import requests
import os

def __get_request(url):
        """Универсальный метод для выполнения GET-запросов"""
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return None


def get_all_employ():
    return __get_request(f"{os.getenv('OK_URL')}v1/employees/list?api_token={os.getenv('OK_TOKEN')}")


def create_okdesk_ticket(object_name,
                         owner, 
                         object_id, 
                         employ,
                         problem_title,
                         problem_desc,
                         type_req
                         ):
    "отправка post запроса на создание заявки ОКДЕСК на приостановку"
    all_empl = get_all_employ()
    concrete_empl = [empl["id"] for empl in all_empl if empl["last_name"] == employ] 

    url=f"{os.getenv('OK_URL')}v1/issues/?api_token={os.getenv('OK_TOKEN')}"
    data = {
            "title": f"{problem_title}",
            "description": f"{problem_title} <b>{object_name}</b> {problem_desc}",
            "company_id": owner,
            "assignee_id": str(concrete_empl[0]) if len(concrete_empl) >= 1 else None,
            "maintenance_entity_id": object_id,
            "type": type_req,
            "custom_parameters":{"ts_quantity":"1","labor_intensity":"2"}
            }
    try:
        response = requests.post(url, json = data)
        if response.status_code == 200:
            return (f"Успешно создана заявка в ОКДЕСК на {problem_title}", True)
        else:
            return (f"Ошибка при создании заявки: {response.text}", False)
    except Exception as e:
            return (f"Ошибка при работе с OkDesk API: {e} --- {data}", False)
