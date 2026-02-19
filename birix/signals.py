from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import DevicesDiagnostics, CaObjects, Devices
import os
import logging

from django.contrib import messages


OKDESK_API_URL = "https://your_okdesk_domain.okdesk.ru/api/v1/issues"
OKDESK_API_KEY = "your_api_key_here"

def create_okdesk_ticket(device):
    "Создание заявки в ОКДЕСК при попадании терминала в ремонт"
    print(device)

    ok_token = os.getenv('OK_TOKEN') 
    ok_url = os.getenv('OK_URL')
    #
    # url=f"{ok_url}v1/issues/?api_token={ok_token}"
    # data = {
    #         "title": f"Приостановить объект, Терминал отправлен в ремонт",
    #         "description": f"",
    #         "company_id": owner,
    #         "deadline_at": str(date.today() + timedelta(days=14)) + " 17:30",
    #         "assignee_id": str(employ[0]),
    #         "maintenance_entity_id": object_id,
    #         "type": "vn_control_dop_obor",
    #         "custom_parameters":{"ts_quantity":"1","labor_intensity":"2"},
    #         "parent_id": ok_issues_id,
    #         }
    #
    # response = requests.post(url, json=data)
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     messages.error(request, f"Не сохранились данные {response.status_code} {response.text} {data}")

@receiver(post_save, sender=DevicesDiagnostics)
def send_okdesk_request(sender, instance, **kwargs):
    """
    Отправляет запрос в OKDESK при изменении поля 'whom_tranfer' на 1 (в ремонт)
    """
    if instance.whom_tranfer == 1:
        request = kwargs.get('request')
        try:
            device = Devices.objects.get(device_id=instance.device_id)

            if device:
                messages.error(request, f"Найден IMEI")
            else:
                messages.error(request, f"НЕ Найден IMEI")

            create_okdesk_ticket(device)
        except Devices.DoesNotExist:
            messages.error(request, f"НЕ ПОЛУЧЕН Девайс")
