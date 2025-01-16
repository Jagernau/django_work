from django import forms
from django.db.models.expressions import fields
from birix.validators import validate_login, validate_password
from birix.models import *
from .models import CaObjects

class NewLoginForm(forms.ModelForm):
    class Meta:
        model = LoginUsers
        fields = [
                'client_name',
                'login',
                'email',
                'password',
                'date_create',
                'system',
                'contragent',
                'comment_field',
                'ca_uid',
                'account_status',
                ]

    def clean_form(self):
        login = self.cleaned_data.get("login")
        if self.instance.pk is None:
            validate_login(login)
        return login

class UploadFileForm(forms.Form):
    object_name = forms.CharField(
        label="Объект",
        widget=forms.TextInput(attrs={'readonly': 'readonly'})  # Делаем поле только для чтения
    )
    file = forms.FileField(label="Файл")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), label="Дата")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'object_name' in kwargs:
            self.fields['object_name'].initial = kwargs.pop('object_name')  # Устанавливаем начальное значение
