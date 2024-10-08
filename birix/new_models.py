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


class Contragents(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_holding = models.ForeignKey('Holdings', models.DO_NOTHING, blank=True, null=True, db_comment='ID холдинга')
    ca_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Название контрагента')
    ca_shortname = models.CharField(max_length=250, blank=True, null=True)
    ca_inn = models.CharField(max_length=60, blank=True, null=True, db_comment='ИНН контрагента')
    ca_kpp = models.CharField(max_length=60, blank=True, null=True, db_comment='КПП контрагента')
    ca_bill_account_num = models.CharField(max_length=60, blank=True, null=True, db_comment='Расчетный счет')
    ca_bill_account_bank_name = models.CharField(max_length=60, blank=True, null=True, db_comment='Наименование банка')
    ca_bill_account_ogrn = models.CharField(max_length=60, blank=True, null=True, db_comment='ОГРН')
    ca_edo_connect = models.IntegerField(blank=True, null=True, db_comment='Обмен ЭДО')
    ca_field_of_activity = models.CharField(max_length=260, blank=True, null=True, db_comment='Сфера деятельности')
    ca_type = models.CharField(max_length=60, blank=True, null=True, db_comment='тип компании')
    unique_onec_id = models.CharField(max_length=100, blank=True, null=True, db_comment='уникальный id в 1С контрагента ')
    registration_date = models.DateField(blank=True, null=True, db_comment='Дата регистрации в 1С')
    key_manager = models.CharField(max_length=200, blank=True, null=True, db_comment='Основной менеджер ')
    actual_address = models.CharField(max_length=300, blank=True, null=True, db_comment='Фактический адрес ')
    registered_office = models.CharField(max_length=300, blank=True, null=True, db_comment='Юридический адрес ')
    phone = models.CharField(max_length=200, blank=True, null=True, db_comment='Телефон ')

    class Meta:
        managed = False
        db_table = 'Contragents'


class LoginUsers(models.Model):
    client_name = models.CharField(max_length=200, blank=True, null=True, db_comment='Старая колонка, при ведении excel таблицы')
    login = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateField(blank=True, null=True)
    system = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='Ключ к системе мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    comment_field = models.CharField(max_length=270, blank=True, null=True, db_comment='Поле с комментариями')
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')
    account_status = models.IntegerField(db_comment='Состояние учётки 0-остановлена, 1-не подтверждена но активна, 2-подтверждена и активна')

    class Meta:
        managed = False
        db_table = 'Login_users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaContacts(models.Model):
    ca_contact_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='id компании')
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


class CaContracts(models.Model):
    contract_id = models.AutoField(primary_key=True)
    ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    contract_type = models.CharField(max_length=50, blank=True, null=True, db_comment='Тип договора')
    contract_num_prefix = models.CharField(max_length=50, blank=True, null=True, db_comment='Префикс номера договора')
    contract_num = models.CharField(max_length=50, blank=True, null=True, db_comment='Номер договора')
    contract_payment_term = models.CharField(max_length=50, blank=True, null=True, db_comment='условия оплаты')
    contract_payment_period = models.CharField(max_length=50, blank=True, null=True, db_comment='Период оплаты')
    contract_start_date = models.DateField(blank=True, null=True, db_comment='Дата заключения договора')
    contract_expired_date = models.DateField(blank=True, null=True, db_comment='Дата завершения договора')

    class Meta:
        managed = False
        db_table = 'ca_contracts'


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


class ClientsInSystemMonitor(models.Model):
    id_in_system_monitor = models.CharField(max_length=200, blank=True, null=True, db_comment='Id клиента в системе мониторинга')
    name_in_system_monitor = models.CharField(max_length=200, blank=True, null=True, db_comment='Имя клиента в системе мониторинга ')
    owner_id_sys_mon = models.CharField(max_length=200, blank=True, null=True, db_comment='Id хозяина в системе мониторинга')
    system_monitor = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='Id системы мониторинга ')
    client = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='id клиента')

    class Meta:
        managed = False
        db_table = 'clients_in_system_monitor'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_serial = models.CharField(max_length=100, blank=True, null=True, db_comment='Серийный номер устройства')
    device_imei = models.CharField(unique=True, max_length=60, blank=True, null=True, db_comment='IMEI устройства')
    client_name = models.CharField(max_length=300, blank=True, null=True, db_comment='Имя клиента')
    terminal_date = models.DateTimeField(blank=True, null=True, db_comment='Дата программирования терминала')
    devices_brand = models.ForeignKey('DevicesBrands', models.DO_NOTHING, blank=True, null=True, db_comment='ID Модели устройства ')
    name_it = models.CharField(max_length=50, blank=True, null=True, db_comment='Имя програмировавшего терминал')
    sys_mon = models.ForeignKey('MonitoringSystem', models.DO_NOTHING, blank=True, null=True, db_comment='ID системы мониторинга')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    coment = models.CharField(max_length=270, blank=True, null=True, db_comment='Коментарии')
    itprogrammer = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class DevicesBrands(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    devices_vendor = models.ForeignKey('DevicesVendor', models.DO_NOTHING, blank=True, null=True, db_comment='Id Вендора терминалов')

    class Meta:
        managed = False
        db_table = 'devices_brands'


class DevicesCommands(models.Model):
    command = models.CharField(max_length=100, blank=True, null=True)
    device_brand = models.ForeignKey(DevicesBrands, models.DO_NOTHING, db_column='device_brand', blank=True, null=True, db_comment='Id брэнда терминала')
    method = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_commands'


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
        db_table_comment = 'Диагностика терминалов'


class DevicesLoggerCommands(models.Model):
    command_date = models.DateTimeField(db_comment='Время отправки команды ')
    command_resresponse = models.CharField(max_length=200, db_comment='Ответ на команду')
    command_send = models.CharField(max_length=200, db_comment='Команда')
    programmer = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='programmer', db_comment='Кто отправил команду')
    terminal_imei = models.CharField(max_length=50, db_comment='imei терминала')

    class Meta:
        managed = False
        db_table = 'devices_logger_commands'
        db_table_comment = 'Таблица логгов команд'


class DevicesVendor(models.Model):
    vendor_name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_vendor'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EquipmentWarehouse(models.Model):
    id_unit = models.BigAutoField(primary_key=True, db_comment='Идентификатор записи')
    add_date = models.DateTimeField(db_comment='Время регистрации добавления товара на склад')
    serial_number = models.CharField(unique=True, max_length=200, db_comment='Серийный номер')
    availability = models.IntegerField(db_comment='Наличие на складе\r\n0- нет в наличии\r\n1- в наличии')
    terminal_model = models.ForeignKey(DevicesBrands, models.DO_NOTHING, blank=True, null=True, db_comment='Реляционный id device')
    sensor = models.ForeignKey('ObjectSensors', models.DO_NOTHING, blank=True, null=True, db_comment='Реляция id')
    delivery_date = models.DateTimeField(blank=True, null=True, db_comment='Дата выдачи')
    client = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='Клиент как в 1С')
    comment = models.CharField(max_length=300, blank=True, null=True)
    whom_issued = models.CharField(max_length=300, db_comment='Кому выдан')
    affiliation = models.IntegerField(db_comment='Принадлежность к подразделению:\r\n0-Сервис\r\n1- мониторинг')

    class Meta:
        managed = False
        db_table = 'equipment_warehouse'
        db_table_comment = 'Таблица склада'


class GlobalLogging(models.Model):
    section_type = models.CharField(max_length=50)
    edit_id = models.IntegerField()
    field = models.CharField(max_length=50)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)
    change_time = models.DateTimeField(blank=True, null=True)
    sys_id = models.IntegerField(blank=True, null=True, db_comment='Система мониторинга')
    action = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_logging'


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


class Holdings(models.Model):
    holding_id = models.AutoField(primary_key=True)
    holding_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holdings'


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


class MonitoringSystem(models.Model):
    mon_sys_id = models.AutoField(primary_key=True)
    mon_sys_name = models.CharField(max_length=60, blank=True, null=True, db_comment='Название системы мониторинга')
    mon_sys_obj_price_suntel = models.IntegerField(blank=True, null=True, db_comment='Стоимость объекта для Сантел')
    mon_sys_ca_obj_price_default = models.IntegerField(blank=True, null=True, db_comment='Базовая стоимость объекта для Контрагента')

    class Meta:
        managed = False
        db_table = 'monitoring_system'


class ObjectRetranslators(models.Model):
    retranslator_id = models.AutoField(primary_key=True)
    retranslator_name = models.CharField(max_length=50, blank=True, null=True, db_comment='Имя ретранслятора')
    retranslator_suntel_price = models.IntegerField(blank=True, null=True)
    retranslator_ca_price = models.IntegerField(blank=True, null=True)
    retrans_adres = models.CharField(max_length=200, blank=True, null=True, db_comment='Адрес куда ретранслируется')
    retrans_protocol = models.IntegerField(db_comment='Виды протоколов:\r\n1- Egts\r\n2 - Wialon ретранслятор\r\n3- Wialon IPS')

    class Meta:
        managed = False
        db_table = 'object_retranslators'


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
    status = models.CharField(max_length=50, blank=True, null=True)
    abon_bool = models.IntegerField(db_comment='На абонентке или нет')

    class Meta:
        managed = False
        db_table = 'object_statuses'


class ObjectVehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_object = models.ForeignKey(CaObjects, models.DO_NOTHING, blank=True, null=True)
    vehicle_ca = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True)
    vehicle_vendor_name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_vendor_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_year_of_manufacture = models.CharField(max_length=255, blank=True, null=True)
    vehicle_gos_nomer = models.CharField(unique=True, max_length=25)
    vehicle_gos_nomer_region = models.CharField(max_length=255, blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True)
    vehicle_vin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_vehicles'


class SensorBrands(models.Model):
    name = models.CharField(max_length=200, db_comment='Название модели')
    sensor_vendor = models.ForeignKey('SensorVendor', models.DO_NOTHING, db_comment='Связь к Фирме изготовителя')

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
    status = models.IntegerField(blank=True, null=True, db_comment='Активность симки:\r\n0-списана, 1-активна, 2-приостан, 3-первичная блокировка, 4-статус неизвестен')
    terminal_imei = models.CharField(max_length=25, blank=True, null=True, db_comment='IMEI терминала в который вставлена симка')
    contragent = models.ForeignKey(Contragents, models.DO_NOTHING, blank=True, null=True, db_comment='ID контрагента')
    ca_uid = models.CharField(max_length=100, blank=True, null=True, db_comment='Уникальный id контрагента')
    itprogrammer = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True, db_comment='ID сотрудника програмировавшего терминал')

    class Meta:
        managed = False
        db_table = 'sim_cards'
