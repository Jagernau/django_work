from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from birix.utils import get_accouns, get_history
from datetime import datetime
from django.contrib import admin
import birix.models as models
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponse
import pandas as pd
from django.contrib.auth.decorators import user_passes_test


@login_required
@user_passes_test(lambda u: u.is_superuser)
def calendar_call(request):
    if request.method == 'POST':
        start = request.POST['start_date']
        end = request.POST['end_date']
        duration_user = request.POST['duration']
        detes = get_history(start, end)
        officers = get_accouns()
        result = []
        ofice_users = models.AuthUser.objects.all()
        contacts = models.CaContacts.objects.all()
        list_last_names = []
        view_user = request.user.username
        concrete_user = models.AuthUser.objects.filter(username=view_user).first()
        for i in ofice_users:
            list_last_names.append(f"{i.last_name} {i.first_name}")

        for i in detes:
            count = len(str(i).split(","))
            if count >= 8:
                if int(str(i).split(",")[7]) >= int(duration_user):
                    clear_date = str(str(i).split(",")[5]).replace("T", " ").replace("Z", "")
                    clear_type = "Входящий звонок" if str(i).split(",")[1] == "in" else "Исходящий звонок"
                    duration = str(i).split(",")[7]
                    h = int(duration) // 3600
                    m = int(duration) % 3600 // 60
                    s = int(duration) % 60

                    clear_duration = f"{h:02d}:{m:02d}:{s:02d}"
                    clear_name = ""
                    name = str(str(i).split(",")[3]).split("@")[0]
                    contact_name = ""
                    contact_position = ""
                    contact_client = ""
                    for o in officers:
                        if name == o["name"]:
                            clear_name = o["realName"]

                    link_head = str(i).split(",")[8]
                    for phone in contacts:
                        if str(str(i).split(",")[2]) == str(phone.ca_contact_cell_num):
                            contact_name = f"{phone.ca_contact_surname} {phone.ca_contact_name}"
                            contact_position = phone.ca_contact_position
                            contact_client = phone.ca.ca_name
                

                    if clear_name in list_last_names:

                        result.append(
                                {
                                    'date': clear_date,
                                    'type': clear_type,
                                    'number': str(i).split(",")[2],
                                    'name': clear_name,
                                    'duration': clear_duration,
                                    "link": link_head,
                                    "contact_name": contact_name,
                                    "contact_position": contact_position,
                                    "contact_client": contact_client
                                }
                                )
        if request.POST.get('number_phone'):
            number_phone = request.POST.get('number_phone')
            result = [i for i in result if i['number'] == number_phone]

        request.session['result'] = result
        request.session['name_file'] = f"Звонки от {start} по {end}"
        return render(request, 'calendar.html', {'results': result})

    else:
        return render(request, 'calendar.html')

@login_required
def download_excel(request):
    result = request.session.get('result')
    name_file = request.session.get('name_file')
    df = pd.DataFrame(result)
    df.to_excel(f'{name_file}.xlsx', index=False)
    with open(f'{name_file}.xlsx', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename={name_file}.xlsx'
        return response

@login_required
def not_present_accounts(request):
    not_present = models.LoginUsers.objects.filter(
       account_status=1,
    ).all()
    results = []
    for i in not_present:
        if i.contragent == None:
            client = "Нет привязки к клиенту 1с"
        else:
            client = i.contragent.ca_name

        results.append(
                {
                    'login': i.login,
                    'client': client,
                    'id': i.id
                }
                )
    return render(request, 'not_present.html', {'results': results})


@login_required
def home(request):
    return render(request, 'home.html')

class UpdateUserView(UpdateView):
    model = models.LoginUsers
    success_message = 'Учётка успешно обновлена'
    fields = ['account_status']
    template_name = 'edit_login.html'
    success_url = '../not_present'

@login_required
def get_contragents_data(request):
    all_contragents = models.Contragents.objects.values("ca_id", "ca_name").distinct()
    all_objects = models.CaObjects.objects.values("id", "contragent", "object_status")
    results = []
    for i in all_contragents:
        abon_count = 0
        test_count = 0
        new_count = 0
        wait_prog = 0
        deact = 0
        for j in all_objects:
            if i["ca_id"] == j["contragent"]:
                if j["object_status"] == 3:
                    abon_count += 1
                if j["object_status"] == 2:
                    test_count += 1
                if j["object_status"] == 1:
                    new_count += 1
                if j["object_status"] == 4:
                    wait_prog += 1
                if j["object_status"] == 7:
                    deact += 1

        results.append(
                {
                    'contragent_name': i["ca_name"],
                    "abon_count": abon_count,
                    "test_count": test_count,
                    "new_count": new_count,
                    "wait_prog": wait_prog,
                    "deact": deact

                }
        )
    sorted_results = sorted(
            results,
            key=lambda a: (a['abon_count'], a['test_count'], a['new_count'], a['wait_prog'], a['deact']), 
            reverse=True
            )
    request.session['result'] = sorted_results
    request.session['name_file'] = f"Контрагенты{datetime.now()}"
                
    return render(request, 'contragents.html', {'results': sorted_results})

class ListLoginsView(ListView):
    model = models.LoginUsers
    template_name = 'list_logins.html'
    context_object_name = 'logins'

    
class DetailLoginsView(DetailView):
    model = models.LoginUsers
    template_name = 'detail_login.html'
    fields = '__all__'
    def get_logins_object(self):
        objects = models.CaObjects.objects.filter(
            owner_user=self.object.login,
            object_status=3
        ).all()
        return objects
    logins_object = property(get_logins_object)
    context_object_name = 'context'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logins_object'] = self.logins_object
        return context
        
def objects(request):
    search_name = request.GET.get('search_name')
    search_imei = request.GET.get('search_imei')
    search_client = request.GET.get('search_client')
    objects = models.CaObjects.objects.all()

    if search_name:
        objects = objects.filter(object_name__icontains=search_name)

        objects = objects.order_by('object_name')

        return render(request, 'objects.html', {'objects': objects})

    elif search_imei:
        objects = objects.filter(imei__icontains=search_imei)

        objects = objects.order_by('object_name')

        return render(request, 'objects.html', {'objects': objects})


    if search_client:
        objects = objects.filter(owner_contragent=search_client)

        objects = objects.order_by('object_name')

        return render(request, 'objects.html', {'objects': objects})

    else:
        page = request.GET.get('page', 1)

        paginator = Paginator(objects, 20)
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        return render(request, 'objects.html', {'objects': objects})


def objects_detail(request, pk):
    object = get_object_or_404(models.CaObjects, pk=pk)
    return render(request, 'objects_detail.html', {'object': object})
