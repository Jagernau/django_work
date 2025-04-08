import requests
import os

from time import sleep
from requests.auth import HTTPBasicAuth

class MtsSender:
    def __init__(self):
        self.login = os.getenv('MTS_API_SMS_LOGIN')
        self.password = os.getenv('MTS_API_SMS_PASSWORD')
        self.naming = os.getenv('MTS_API_SMS_NAMING')

    
    def __check_message_deliver(self, message_id):
        'Отдаёт код ответа успешности доставки'
        sleep(2)
        url = 'https://omnichannel.mts.ru/http-api/v1/messages/info'
        body = {"int_ids": [message_id]}
        resp_info = requests.post(url , json=body, auth=HTTPBasicAuth(self.login, self.password))
        if resp_info.status_code == 200:
            result = resp_info.json()
            result_code = result["events_info"][0]["events_info"][-1]["status"]
            if result_code == 300:
                return "Доставлено"
            if result_code == 301:
                return "Не доставлено"
            else:
                return "Статус доставки не известен, не прогрузилось"
        else:
            return "Не доставлено"

    def __check_message_send(self, message_id):
        'Отдаёт код ответа успешности отправки'
        sleep(3)
        url = 'https://omnichannel.mts.ru/http-api/v1/messages/info'
        body = {"int_ids": [message_id]}
        resp_info = requests.post(url , json=body, auth=HTTPBasicAuth(self.login, self.password))
        if resp_info.status_code == 200:
            result = resp_info.json()
            result_code = result["events_info"][0]["events_info"][0]["status"]
            if result_code == 200:
                sleep(1)
                return (True, f"Успешно отправленно")
            else:
                return (False, f"Не отправленно")
        else:
            return (False, f"Ошибка в получении статуса")


    def send_message(self, tel_num, text_mess):
        'Отправка сообщения на терминал по номеру телефона'
        sleep(1)
        url = 'https://omnichannel.mts.ru/http-api/v1/messages'
        body = {
        "messages": [
        {
        "content": {
        "short_text": text_mess
        },
        "from": {
        "sms_address": self.naming
        },
        "to": [
        {
        "msisdn": tel_num
        }
        ]
        }]
        }
        resp = requests.post(url, json=body, auth = HTTPBasicAuth(self.login, self.password))
        if resp.status_code == 200:
            result = resp.json()
            mess_id = result['messages'][0]['internal_id']
            sleep(2)
            res_send = self.__check_message_send(mess_id)
            sleep(2)
            res_deliver = self.__check_message_deliver(mess_id)
            return (res_send[0], f'{str(res_send[1])} + {str(res_deliver)}')


        else:
            return (False, f"{resp.status_code} {resp.text}")


