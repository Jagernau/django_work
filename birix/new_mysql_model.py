# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CellOperator(models.Model):
    name = models.CharField(max_length=60, db_comment='Имя сотового оператора')
    ca_price = models.IntegerField(blank=True, null=True, db_comment='цена для клиентов')
    sun_price = models.IntegerField(blank=True, null=True, db_comment='Цена для Сантел')

    class Meta:
        managed = False
        db_table = 'Cell_operator'
        db_table_comment = 'Таблица для хранения информации об операторах сотовой связи'


class Contragents(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_holding = models.ForeignKey('Holdings', models.DO_NOTHING, blank=True, null=True, db_comment='ID холдинга')
    ca_name = models.CharField(max_length=255, blank=True, null=True, db_comment='НаименованиеПартнёра')
    ca_shortname = models.CharField(max_length=250, blank=True, null=True, db_comment='НаименованиеПолноеПартнёра')
    ca_inn = models.CharField(max_length=60, blank=True, null=True, db_comment='ИНН')
    ca_kpp = models.CharField(max_length=60, blank=True, null=True, db_comment='КПП')
    ca_bill_account_num = models.CharField(max_length=60, blank=True, null=True, db_comment='Расчетный счет ????????')
    ca_bill_account_bank_name = models.CharField(max_length=60, blank=True, null=True, db_comment='Наименование банка ????')
    ca_bill_account_ogrn = models.CharField(max_length=60, blank=True, null=True, db_comment='ОГРН ????????')
    ca_edo_connect = models.IntegerField(blank=True, null=True, db_comment='Обмен ЭДО ??????')
    ca_field_of_activity = models.CharField(max_length=260, blank=True, null=True, db_comment='НаправлениеБизнесаКонтрагента')
    ca_type = models.CharField(max_length=60, blank=True, null=True, db_comment='ЮрФизЛицоПартёр')
    unique_onec_id = models.CharField(max_length=100, blank=True, null=True, db_comment='УникальныйИдентификаторПарнёра')
    registration_date = models.DateField(blank=True, null=True, db_comment='Дата регистрации в 1С')
    key_manager = models.CharField(max_length=200, blank=True, null=True, db_comment='Основной менеджер ')
    actual_address = models.CharField(max_length=300, blank=True, null=True, db_comment='Фактический адрес ')
    registered_office = models.CharField(max_length=300, blank=True, null=True, db_comment='Юридический адрес ')
    phone = models.CharField(max_length=200, blank=True, null=True, db_comment='Телефон ')
    ca_uid_contragent = models.CharField(max_length=100, blank=True, null=True, db_comment='УникальныйИдентификаторКонтрагента')
    ca_name_contragent = models.CharField(max_length=255, blank=True, null=True, db_comment='НаименованиеКонтрагента')
    service_manager = models.CharField(max_length=100, blank=True, null=True, db_comment='Имя прикреплённого менеджера тех поддержки')

    class Meta:
        managed = False
        db_table = 'Contragents'
        db_table_comment = 'Таблица для хранения информации о контрагентах по тз'


class LoginUsers(models.Model):
    client_name = models.CharField(max_length=200, blank=True, null=True, db_comment='Старая колонка, при ведении excel таблицы')
    login = models.CharField(max_length=60, blank=True, null=True, db_comment='логин')
    email = models.CharField(max_length=60, blank=True, null=True, db_comment='почта')
    password = models.CharField(max_length=60, blank=True, null=True, db_comment='пароль')
    date_create = models.DateField(blank=True, null=True, db_comment='дата создания')
    system = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='Ключ к системе мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    comment_field = models.CharField(max_length=270, blank=True, null=True, db_comment='Поле с комментариями')
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')
    account_status = models.IntegerField(db_comment='Состояние учётки 0-остановлена, 1-не подтверждена но активна, 2-подтверждена и активна 3 -тестовая')

    class Meta:
        managed = False
        db_table = 'Login_users'
        db_table_comment = 'Таблица для хранения информации о пользователях систем мониторинга'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_comment='Название группы пользователей ЦМС')

    class Meta:
        managed = False
        db_table = 'auth_group'
        db_table_comment = 'Таблица для хранения групп пользователей ЦМС'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, db_comment='Связь с группой пользователей ЦМС')
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING, db_comment='Связь с разрешениями действий в ЦМС')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
        db_table_comment = 'Таблица связи групп пользователей ЦМС с разрешениями'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_comment='Название разрешения для пользователя ЦМС')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, db_comment='Возможность выполнять действия в ЦМС')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
        db_table_comment = 'Таблица разрешений для пользователей ЦМС'


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_comment='пароль')
    last_login = models.DateTimeField(blank=True, null=True, db_comment='последний вход')
    is_superuser = models.IntegerField(db_comment='принадлежность к суперпользователю')
    username = models.CharField(unique=True, max_length=150, db_comment='логин')
    first_name = models.CharField(max_length=150, db_comment='имя')
    last_name = models.CharField(max_length=150, db_comment='фамилия')
    email = models.CharField(max_length=254, db_comment='почта')
    is_staff = models.IntegerField(db_comment='является ли сотрудником')
    is_active = models.IntegerField(db_comment='активность аккаунта')
    date_joined = models.DateTimeField(db_comment='дата создания аккаунта')

    class Meta:
        managed = False
        db_table = 'auth_user'
        db_table_comment = 'Таблица пользователей ЦМС'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_comment='связь с пользователем ЦМС')
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, db_comment='связь с группой пользователей ЦМС')

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
        db_table_comment = 'Таблица связи пользователей с группами в системе аутентификации ЦМС'


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        db_table_comment = 'Таблица связи пользователей с разрешениями в системе аутентификации ЦМС'


class CaContacts(models.Model):
    ca_contact_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='связь с id компании')
    ca_contact_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Имя контактного лица')
    ca_contact_surname = models.CharField(max_length=255, blank=True, null=True, db_comment='Фамилия контактного лица')
    ca_contact_middlename = models.CharField(max_length=255, blank=True, null=True, db_comment='Отчество контактного лица')
    ca_contact_cell_num = models.CharField(unique=True, max_length=255, blank=True, null=True, db_comment='Сотовый телефон контакт. лица')
    ca_contact_work_num = models.CharField(max_length=255, blank=True, null=True, db_comment='Рабочий телефон к.л.')
    ca_contact_email = models.CharField(max_length=255, blank=True, null=True, db_comment='Электр.почт. к.л')
    ca_contact_position = models.CharField(max_length=255, blank=True, null=True, db_comment='Должность к.л.')

    class Meta:
        managed = False
        db_table = 'ca_contacts'
        db_table_comment = 'Таблица для хранения контактной информации Клиентов по тз'


class CaContracts(models.Model):
    contract_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    contract_type = models.CharField(max_length=50, blank=True, null=True, db_comment='Тип договора\r\nя бы сделал choice')
    contract_num_prefix = models.CharField(max_length=50, blank=True, null=True, db_comment='Префикс номера договора')
    contract_num = models.CharField(max_length=50, blank=True, null=True, db_comment='Номер договора')
    contract_payment_term = models.CharField(max_length=50, blank=True, null=True, db_comment='условия оплаты')
    contract_payment_period = models.CharField(max_length=50, blank=True, null=True, db_comment='Период оплаты')
    contract_start_date = models.DateField(blank=True, null=True, db_comment='Дата заключения договора')
    contract_expired_date = models.DateField(blank=True, null=True, db_comment='Дата завершения договора')

    class Meta:
        managed = False
        db_table = 'ca_contracts'
        db_table_comment = 'Таблица для хранения информации о контрактах по тз'


class CaObjects(models.Model):
    sys_mon = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='ID системы мониторинга')
    sys_mon_object_id = models.CharField(max_length=50, blank=True, null=True, db_comment='ID объекта в системе мониторинга. Единственное за что можно зацепиться')
    object_name = models.CharField(max_length=70, blank=True, null=True, db_comment='Название объекта')
    object_status = models.ForeignKey('ObjectStatuses', models.DO_NOTHING, db_column='object_status', blank=True, null=True, db_comment='Статус объекта ссылается к статусам')
    object_add_date = models.DateTimeField(blank=True, null=True, db_comment='Дата добавления объекта')
    object_last_message = models.DateTimeField(blank=True, null=True, db_comment='Дата последнего сообщения')
    object_margin = models.IntegerField(blank=True, null=True, db_comment='Надбавка к базовой цене объекта')
    owner_contragent = models.CharField(max_length=200, blank=True, null=True, db_comment='Хозяин контрагент, как в системе мониторинга.')
    owner_user = models.CharField(max_length=255, blank=True, null=True, db_comment='Хозяин юзер. Логин пользователя в системе мониторинга')
    imei = models.CharField(max_length=100, blank=True, null=True, db_comment='идентификатор терминала')
    updated = models.DateTimeField(blank=True, null=True, db_comment='Когда изменён')
    object_created = models.DateTimeField(blank=True, null=True, db_comment='Дата создания в системе мониторинга ')
    parent_id_sys = models.CharField(max_length=200, blank=True, null=True, db_comment='Id клиента в системе мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True)
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')

    class Meta:
        managed = False
        db_table = 'ca_objects'
        db_table_comment = 'Таблица для хранения информации об объектах из систем мониторинга'


class ClientsInSystemMonitor(models.Model):
    id_in_system_monitor = models.CharField(max_length=200, blank=True, null=True, db_comment='Id клиента в системе мониторинга')
    name_in_system_monitor = models.CharField(max_length=200, blank=True, null=True, db_comment='Имя клиента в системе мониторинга ')
    owner_id_sys_mon = models.CharField(max_length=200, blank=True, null=True, db_comment='Id хозяина в системе мониторинга')
    system_monitor = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='Id системы мониторинга ')
    client = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='id клиента')

    class Meta:
        managed = False
        db_table = 'clients_in_system_monitor'
        db_table_comment = 'Таблица для хранения информации об id клиентов и id родителей клиентов в СМ не по ТЗ'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_serial = models.CharField(unique=True, max_length=100, db_comment='Серийный номер устройства')
    device_imei = models.CharField(unique=True, max_length=60, blank=True, null=True, db_comment='IMEI устройства')
    client_name = models.CharField(max_length=300, blank=True, null=True, db_comment='Имя клиента')
    terminal_date = models.DateTimeField(blank=True, null=True, db_comment='Дата программирования терминала')
    devices_brand = models.ForeignKey('DevicesBrands', models.DO_NOTHING, blank=True, null=True, db_comment='ID Модели устройства ')
    name_it = models.CharField(max_length=50, blank=True, null=True, db_comment='Имя програмировавшего терминал не актуальна')
    sys_mon = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='ID системы мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    coment = models.CharField(max_length=270, blank=True, null=True, db_comment='Коментарии')
    itprogrammer = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True, db_comment='ссылается к программистам')
    device_owner = models.IntegerField(blank=True, null=True, db_comment='Принадлежность терминала:\r\n--1 МЫ\r\n--0 Клиент')

    class Meta:
        managed = False
        db_table = 'devices'
        db_table_comment = 'Таблица для хранения информации об устройствах запрограммированных IT отделом не по тз'


class DevicesBrands(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    devices_vendor = models.ForeignKey('DevicesVendor', models.DO_NOTHING, blank=True, null=True, db_comment='Id Вендора терминалов')

    class Meta:
        managed = False
        db_table = 'devices_brands'
        db_table_comment = 'Таблица для хранения информации о моделях устройств'


class DevicesCommands(models.Model):
    command = models.CharField(max_length=100, blank=True, null=True, db_comment='сама команда')
    device_brand = models.ForeignKey(DevicesBrands, models.DO_NOTHING, db_column='device_brand', blank=True, null=True, db_comment='Id брэнда терминала')
    method = models.CharField(max_length=10, blank=True, null=True, db_comment='тип отправки команды\r\n0 - смс\r\n1 - интернет\r\n2 - любым')
    description = models.CharField(max_length=300, blank=True, null=True, db_comment='описание действия команды')

    class Meta:
        managed = False
        db_table = 'devices_commands'
        db_table_comment = 'Таблица для хранения информации о командах для устройств не по ТЗ'


class DevicesDiagnostics(models.Model):
    device = models.ForeignKey(Devices, models.DO_NOTHING, db_comment='Отношение к терминалам')
    programmer = models.ForeignKey(AuthUser, models.DO_NOTHING, db_comment='Отношение к программистам')
    brought = models.IntegerField(db_comment='Принесён:\r\n0-от клиента\r\n1-после ремонта')
    comment = models.CharField(max_length=300, db_comment='Коментарий')
    accept_date = models.DateTimeField(db_comment='Дата приёма')
    transfer_date = models.DateTimeField(blank=True, null=True, db_comment='Дата передачи')
    whom_tranfer = models.IntegerField(blank=True, null=True, db_comment='Куда отдан:\r\n0 - клиенту\r\n1 - в ремонт')

    class Meta:
        managed = False
        db_table = 'devices_diagnostics'
        db_table_comment = 'Таблица для хранения информации о диагностике устройств не по тз'


class DevicesLoggerCommands(models.Model):
    command_date = models.DateTimeField(db_comment='Время отправки команды ')
    command_resresponse = models.CharField(max_length=200, db_comment='Ответ на команду')
    command_send = models.CharField(max_length=200, db_comment='Команда')
    programmer = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='programmer', db_comment='Кто отправил команду')
    terminal_imei = models.CharField(max_length=50, db_comment='imei терминала')

    class Meta:
        managed = False
        db_table = 'devices_logger_commands'
        db_table_comment = 'Таблица для хранения журнала команд, отправленных на устройства через ЦМС не по ТЗ'


class DevicesVendor(models.Model):
    vendor_name = models.CharField(max_length=35, blank=True, null=True, db_comment='Название фирмы производителя терминалов')

    class Meta:
        managed = False
        db_table = 'devices_vendor'
        db_table_comment = 'Таблица для хранения информации о производителях устройств'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField(db_comment='Время операции')
    object_id = models.TextField(blank=True, null=True, db_comment='id объекта Бд было произведено действие')
    object_repr = models.CharField(max_length=200, db_comment='что было изменено')
    action_flag = models.PositiveSmallIntegerField(db_comment='какое действие было выполнено')
    change_message = models.TextField(db_comment='на что изменено')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True, db_comment='в какой таблице были изменения')
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_comment='кто из пользователей ЦМС внёс изменения')

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        db_table_comment = 'Таблица для хранения журнала действий администратора ЦМС'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_comment='из какого приложения')
    model = models.CharField(max_length=100, db_comment='из какой модели')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        db_table_comment = 'Таблица для хранения типов содержимого Django ЦМС'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_comment='таблица')
    name = models.CharField(max_length=255, db_comment='действие')
    applied = models.DateTimeField(db_comment='дата')

    class Meta:
        managed = False
        db_table = 'django_migrations'
        db_table_comment = 'Таблица для хранения информации о миграциях Django ЦМС'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        db_table_comment = 'Таблица для хранения сессий Django Заходов в ЦМС'


class EquipmentWarehouse(models.Model):
    id_unit = models.BigAutoField(primary_key=True, db_comment='Идентификатор записи')
    add_date = models.DateTimeField(db_comment='Время регистрации добавления товара на склад')
    serial_number = models.CharField(unique=True, max_length=200, db_comment='Серийный номер')
    availability = models.IntegerField(db_comment='Наличие на складе\r\n0- нет в наличии\r\n1- в наличии')
    terminal_model = models.ForeignKey(DevicesBrands, models.DO_NOTHING, blank=True, null=True, db_comment='Реляционный id device')
    sensor = models.ForeignKey('SensorBrands', models.DO_NOTHING, blank=True, null=True, db_comment='Реляция id к датчикам')
    delivery_date = models.DateTimeField(blank=True, null=True, db_comment='Дата выдачи')
    client = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='Клиент как в 1С')
    comment = models.CharField(max_length=300, blank=True, null=True, db_comment='коментарий')
    whom_issued = models.CharField(max_length=300, db_comment='Кому выдан')
    affiliation = models.IntegerField(db_comment='Принадлежность к подразделению:\r\n0-Сервис\r\n1- мониторинг')

    class Meta:
        managed = False
        db_table = 'equipment_warehouse'
        db_table_comment = 'Таблица склада'


class GlobalLogging(models.Model):
    section_type = models.CharField(max_length=50, db_comment='изменения в объектах или клиентах')
    edit_id = models.IntegerField(db_comment='id изменённого')
    field = models.CharField(max_length=50, db_comment='поле изменения')
    old_value = models.CharField(max_length=255, blank=True, null=True, db_comment='старое значение')
    new_value = models.CharField(max_length=255, blank=True, null=True, db_comment='новое значение')
    change_time = models.DateTimeField(blank=True, null=True)
    sys_id = models.IntegerField(blank=True, null=True, db_comment='Система мониторинга')
    action = models.CharField(max_length=100, blank=True, null=True, db_comment='добавление, изменение или удаление')
    contragent_id = models.IntegerField(blank=True, null=True, db_comment='логгирование контрагента')

    class Meta:
        managed = False
        db_table = 'global_logging'
        db_table_comment = 'Первоначальная Таблица для хранения изменений в таблицах объектов и клиентов 1с через Python, до тригерного логирования'


class GroupObjectRetrans(models.Model):
    id_group = models.AutoField(primary_key=True, db_comment='Айдишник')
    obj = models.ForeignKey(CaObjects, models.DO_NOTHING, db_comment='Айдишник объекта')
    retr = models.ForeignKey('ObjectRetranslators', models.DO_NOTHING, db_comment='Айдишник ретранслятора')

    class Meta:
        managed = False
        db_table = 'group_object_retrans'
        db_table_comment = 'Таблица для сведения объектов и ретрансляторов'


class GuaranteeTerms(models.Model):
    gt_id = models.AutoField(primary_key=True, db_comment='ID гарантийного срока')
    gt_term = models.IntegerField(blank=True, null=True, db_comment='Срок гарантии (дней)')
    gt_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Тип гарантии')

    class Meta:
        managed = False
        db_table = 'guarantee_terms'
        db_table_comment = 'Таблица для хранения родителей контрагентов'


class Holdings(models.Model):
    holding_id = models.AutoField(primary_key=True)
    holding_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Имя родителя контрагента (Холдинг)')

    class Meta:
        managed = False
        db_table = 'holdings'
        db_table_comment = 'Таблица для хранения информации о Холдингах по тз'


class InfoServObj(models.Model):
    serv_obj_id = models.AutoField(primary_key=True, db_comment='ID подписки')
    serv_obj_sys_mon = models.ForeignKey(CaObjects, models.DO_NOTHING, db_comment='Внутренний ID объекта\r\nБазы данных из СМ')
    info_obj_serv = models.ForeignKey('InformationServices', models.DO_NOTHING, db_comment='ID ведёт сервисам')
    subscription_start = models.DateTimeField(db_comment='Время начала подписки')
    subscription_end = models.DateTimeField(blank=True, null=True, db_comment='Время окончания подписки')
    tel_num_user = models.CharField(max_length=11, blank=True, null=True, db_comment='Телефонный номер с которого созданна услуга')
    service_counter = models.IntegerField(db_comment='СЧЁТЧИК услуг\r\n0- мгновенно\r\n1-раз в день\r\n2-раз в неделю\r\n3-раз в месяц')
    stealth_type = models.IntegerField(db_comment='0 - автоматический\r\n1 - с проверкой')
    monitoring_sys = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, db_column='monitoring_sys', db_comment='Система мониторинга')
    sys_id_obj = models.CharField(max_length=100, db_comment='ID объекта в системе мониторинга')
    sys_login = models.CharField(max_length=100, db_comment='Логин пользователя от системы мониторинга')
    sys_password = models.CharField(max_length=100, db_comment='Пароль пользователя от СМ')

    class Meta:
        managed = False
        db_table = 'info_serv_obj'
        db_table_comment = 'Объекты с информационными сервисами'


class InformationServices(models.Model):
    serv_id = models.AutoField(primary_key=True, db_comment='ID Сервиса')
    serv_name = models.CharField(unique=True, max_length=100, db_comment='Название сервиса')
    serv_price = models.IntegerField(blank=True, null=True, db_comment='Цена за сервис')

    class Meta:
        managed = False
        db_table = 'information_services'
        db_table_comment = 'Таблица для информационных сервисов Клиентов'


class Invoicing(models.Model):
    invoic_id = models.AutoField(primary_key=True)
    system_monitorig = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, db_comment='Связь к системе мониторинга из ПУКС')
    system_object_id = models.CharField(max_length=200, db_comment='ID в системе мониторинга из ПУКС')
    puks_tarif = models.IntegerField(blank=True, null=True, db_comment='Тариф из ПУКС')
    add_time = models.DateTimeField(db_comment='дата')

    class Meta:
        managed = False
        db_table = 'invoicing'
        db_table_comment = 'Таблица для хранения информации о счетах-фактурах по объекту вытащенный из другой БД postgres'


class LogChanges(models.Model):
    log_id = models.AutoField(primary_key=True)
    changes_date = models.DateTimeField(blank=True, null=True, db_comment='Дата изменения')
    changes_table = models.CharField(max_length=250, blank=True, null=True, db_comment='В какой таблице были внесены изменения')
    changes_action = models.IntegerField(blank=True, null=True, db_comment='Название действия:\r\n0 - Del\r\n1 - Insert\r\n2 - Update')
    obj_key = models.IntegerField(blank=True, null=True, db_comment='Ключ элемента, Практически везде ID. Делаю по ID int')
    changes_column = models.CharField(max_length=255, blank=True, null=True, db_comment='Название столбца')
    old_val = models.CharField(max_length=255, blank=True, null=True, db_comment='Старое значение')
    new_val = models.CharField(max_length=255, blank=True, null=True, db_comment='Новое значение')

    class Meta:
        managed = False
        db_table = 'log_changes'
        db_table_comment = 'Таблица логирования изменений в данных Базы'


class LoginUsersPhones(models.Model):
    phone = models.CharField(max_length=12, db_comment='телефон')
    login = models.CharField(max_length=12, db_comment='Логин')
    password = models.CharField(max_length=19, db_comment='Пароль')
    mess_name = models.CharField(max_length=40, db_comment='Имя в месседжере')
    mess_user_id = models.CharField(max_length=100, db_comment='ID в меседжере')

    class Meta:
        managed = False
        db_table = 'login_users_phones'
        db_table_comment = 'Таблица с логинами и паролями и телефонами'


class MonitoringSystem(models.Model):
    mon_sys_id = models.AutoField(primary_key=True)
    mon_sys_name = models.CharField(max_length=60, blank=True, null=True, db_comment='Название системы мониторинга')
    mon_sys_obj_price_suntel = models.IntegerField(blank=True, null=True, db_comment='Стоимость объекта для Сантел')
    mon_sys_ca_obj_price_default = models.IntegerField(blank=True, null=True, db_comment='Базовая стоимость объекта для Контрагента')
    mon_url = models.CharField(max_length=200, blank=True, null=True, db_comment='Адресс Системы мониторинга')

    class Meta:
        managed = False
        db_table = 'monitoring_system'
        db_table_comment = 'Таблица для хранения информации о системах мониторинга'


class ObjectRetranslators(models.Model):
    retranslator_id = models.AutoField(primary_key=True)
    retranslator_name = models.CharField(max_length=50, blank=True, null=True, db_comment='Имя ретранслятора')
    retranslator_suntel_price = models.IntegerField(blank=True, null=True, db_comment='цена ретрансляции для Сантел')
    retranslator_ca_price = models.IntegerField(blank=True, null=True, db_comment='Цена ретрансляции для клиента')
    retrans_adres = models.CharField(max_length=200, blank=True, null=True, db_comment='Адрес куда ретранслируется')
    retrans_protocol = models.IntegerField(db_comment='Виды протоколов:\r\n1- Egts\r\n2 - Wialon ретранслятор\r\n3- Wialon IPS')

    class Meta:
        managed = False
        db_table = 'object_retranslators'
        db_table_comment = 'Таблица для хранения информации о ретрансляторах'


class ObjectSensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    sensor_type = models.IntegerField(db_comment='Тип датчика:\r\n1ДУТ, 2Температуры3наклона')
    sensor_model = models.ForeignKey('SensorBrands', models.DO_NOTHING, blank=True, null=True, db_comment='Модель датчика к моделям')
    sensor_technology = models.IntegerField(db_comment='Подтип датчика:\r\n1аналоговый,2цифровой,\r\n3частотный')
    sensor_connect_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Тип подключения')
    client = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='Связь с id Клиента')
    sensor_serial = models.CharField(unique=True, max_length=100, blank=True, null=True, db_comment='Серийный номер датчика')
    name_installer = models.CharField(max_length=150, blank=True, null=True, db_comment='Имя монтажника')
    installer_id = models.IntegerField(blank=True, null=True, db_comment='Id монтажника')

    class Meta:
        managed = False
        db_table = 'object_sensors'
        db_table_comment = 'Датчик'


class ObjectStatuses(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True, db_comment='Название статуса')
    abon_bool = models.IntegerField(db_comment='На абонентке или нет')

    class Meta:
        managed = False
        db_table = 'object_statuses'
        db_table_comment = 'Таблица для хранения информации о статусах объектов'


class ObjectVehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_object = models.ForeignKey(CaObjects, models.DO_NOTHING, blank=True, null=True, db_comment='привязка к объекту')
    vehicle_ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='привязка к контрагенту')
    vehicle_vendor_name = models.CharField(max_length=255, blank=True, null=True, db_comment='производитель тс')
    vehicle_vendor_model = models.CharField(max_length=255, blank=True, null=True, db_comment='марка тс')
    vehicle_year_of_manufacture = models.CharField(max_length=255, blank=True, null=True, db_comment='дата выпуска тс')
    vehicle_gos_nomer = models.CharField(unique=True, max_length=25, db_comment='госномер')
    vehicle_gos_nomer_region = models.CharField(max_length=255, blank=True, null=True, db_comment='регион')
    vehicle_type = models.CharField(max_length=255, blank=True, null=True, db_comment='тип тс')
    vehicle_vin = models.CharField(max_length=255, blank=True, null=True, db_comment='вин')

    class Meta:
        managed = False
        db_table = 'object_vehicles'
        db_table_comment = 'Таблица для хранения информации об объектах-транспортных средствах'


class SensorBrands(models.Model):
    name = models.CharField(max_length=200, db_comment='Название модели')
    sensor_vendor = models.ForeignKey('SensorVendor', models.DO_NOTHING, db_comment='Связь к Фирме изготовителя')
    model_type = models.IntegerField(blank=True, null=True, db_comment='Тип датчика: \r\n1 ДУТ.\r\n2 Температуры.\r\n3 Наклона.\r\n4 Индикатор.')

    class Meta:
        managed = False
        db_table = 'sensor_brands'
        db_table_comment = 'Таблица моделей датчиков'


class SensorVendor(models.Model):
    name = models.CharField(max_length=200, db_comment='Имя производителя')

    class Meta:
        managed = False
        db_table = 'sensor_vendor'
        db_table_comment = 'Производители датчиков'


class SimCards(models.Model):
    sim_id = models.AutoField(primary_key=True)
    sim_iccid = models.CharField(unique=True, max_length=40, blank=True, null=True, db_comment='ICCID')
    sim_tel_number = models.CharField(max_length=40, blank=True, null=True, db_comment='телефонный номер сим')
    client_name = models.CharField(max_length=270, blank=True, null=True, db_comment='Имя клиента')
    sim_cell_operator = models.ForeignKey(CellOperator, models.DO_NOTHING, db_column='sim_cell_operator', blank=True, null=True, db_comment='Сотовый оператор(надо по ID)')
    sim_owner = models.IntegerField(blank=True, null=True, db_comment="1, 'Мы'\r\n0, 'Клиент'")
    sim_device = models.ForeignKey(Devices, models.DO_NOTHING, blank=True, null=True, db_comment='ID к девайсам(devices)')
    sim_date = models.DateTimeField(blank=True, null=True, db_comment='Дата регистрации сим')
    status = models.IntegerField(blank=True, null=True, db_comment='Активность симки:\r\n0-списана, 1-активна, 2-приостан, 3-первичная блокировка, 4-статус неизвестен,\r\n5 - Сезонная блокировка')
    terminal_imei = models.CharField(max_length=25, blank=True, null=True, db_comment='IMEI терминала в который вставлена симка')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')
    itprogrammer = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True, db_comment='ID сотрудника програмировавшего терминал')
    block_start = models.DateTimeField(blank=True, null=True, db_comment='Начало блокировки')
    block_end = models.DateTimeField(blank=True, null=True, db_comment='Предварительный конец блокировки')

    class Meta:
        managed = False
        db_table = 'sim_cards'


class UserLogging(models.Model):
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action_type = models.CharField(max_length=50, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    action_time = models.TimeField(blank=True, null=True)
    old_val = models.TextField(blank=True, null=True)
    new_val = models.CharField(max_length=300, blank=True, null=True)
    action_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_logging'
        db_table_comment = 'Таблица для хранения логов действий пользователей Базы данных, например пользователя Битрикс или Разработчиков Махалова'
