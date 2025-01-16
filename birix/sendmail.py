from django.core.mail import send_mail

def sendmailmanager(email, username, password, client_name, system_url, proger):
    # Заголовок письма
    subject = f'Данные для входа в систему мониторинга для {client_name}'
    # Текст письма
    message = f'Учётную запись создал: {proger}\nЛогин: {username}\nПароль: {password}\nСсылка на систему мониторинга: {system_url}\nПисьмо отправлено автоматически.'
    # Отправитель
    from_email = 'y.kuftov@suntel-nn.ru'
    # Получатель
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

def sendmailclient(email, username, password, mon_system, system_url):
    # Заголовок письма
    subject = f'Данные для входа в систему мониторинга {mon_system}'
    # Текст письма
    message = f'Логин: {username}\nПароль: {password}\nСсылка на систему мониторинга: {system_url}\n'
    if mon_system == 'Glonasssoft':
        message = message + 'Ссылки на мобильные версии:\nApp Store: https://apps.apple.com/ru/app/glonasssoft/id1503150794\nGoogle Play: https://play.google.com/store/apps/details?id=ru.glonasssoft.hosting\nОбучающее видео: https://suntel-nn.ru/images/cms/data/v..._sajta.mp4\n'
    elif mon_system == 'Fort monitor':
        message = message + 'Ссылки на мобильные версии:\nApp Store: https://apps.apple.com/ru/app/fort-monitor/id1445831699\nGoogle Play: https://play.google.com/store/apps/details?id=com.fort_telecom.fortmonitor\n'
    message = message + '\nПисьмо отправлено автоматически.\nТелефон для справок: 8 (831) 218-03-16'
    # Отправитель
    from_email = 'y.kuftov@suntel-nn.ru'
    # Получатель
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
