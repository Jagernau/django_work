from django.contrib import admin
from birix.models import *
from django.contrib.admin import DateFieldListFilter

class ContragentsAdmin(admin.ModelAdmin):
    list_display = (
            "ca_name", 
            "ca_shortname",
            "ca_inn",
            "ca_kpp",           
            )
    list_filter = (
            "ca_name",
            "ca_inn",
            )
    search_fields = (
            "ca_name",
            "ca_inn",
            "ca_kpp",       
            )

    fieldsets = (
            (None, {
                'fields': (
                    'ca_name',
                    'ca_shortname',
                    'ca_inn',
                    'ca_kpp',
                )
            }),
        
        )

class LoginUsersAdmin(admin.ModelAdmin):
    list_display = (
            "client_name",
            "login",
            "email",
            "password",
            "date_create",
            "system",
            "contragent",
            "comment_field",
            )

    list_filter = (
            "system",
            "contragent",
            "contragent",
            )
    search_fields = (
            "client_name",
            "login",
            "comment_field",
            "contragent__ca_id",
    )

    fieldsets = (
            (None, {
                'fields': (
                    'client_name',
                    'login',
                    'email',
                    'password',
                    'date_create',
                    'system',
                    'contragent',
                    'comment_field',
                )
            }),
    )

    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'client_name',
                    'login',
                    'email',
                    'password',
                    'date_create',
                    'system',
                    'contragent',
                    'comment_field',
                )
            })
    )
    raw_id_fields = ('contragent',)

class CaObjectsAdmin(admin.ModelAdmin):
    list_display = (
            "sys_mon",
            "object_name",
            "object_status",
            "owner_contragent",
            "owner_user",
            "contragent",
            "imei",
            )

    list_filter = (
            "object_status",
            "sys_mon",
#            "contragent",
#            "object_status",
#            "contragent",
            )
    search_fields = (
            "object_name",
            "contragent__ca_id",
#            "object_status__status_id",
            "owner_user",
            "owner_contragent",
            "imei",
    )

    fieldsets = (
            (None, {
                'fields': (
                    'sys_mon',
                    'object_name',
                    'object_status',
                    'owner_contragent',
                    'owner_user',
                    'contragent',
                )
            }),
    )

class GlobalLogAdmin(admin.ModelAdmin):
    list_display = (
            "section_type",
            "edit_id",
            "field",
            "old_value",
            "new_value",
            "change_time",
            "sys_id",
            "action",
            )

    list_filter = (
            "section_type",
            "edit_id",
            "field",
            )
    search_fields = (
            "section_type",
            "edit_id",
            "field",
            "old_value",
            "new_value",
            "change_time",
            "sys_id",
            "action",
            )
    fieldsets = (
            (None, {
                'fields': (
                    'section_type',
                    'edit_id',
                    'field',
                    'old_value',
                    'new_value',
                    'change_time',
                    'sys_id',
                    'action',
                )
            }),
    )

class SimCardsAdmin(admin.ModelAdmin):
    list_display = (
            "sim_iccid",
            "sim_tel_number",
            "client_name",
            "sim_cell_operator",
            "sim_owner",
            "sim_date",
            "contragent",
            "terminal_imei",
            'itprogrammer',

            )

    list_filter = (
            "sim_cell_operator",
            "sim_owner",
            "sim_date",
#            "contragent",
            'itprogrammer',

            )
    search_fields = (
            "sim_iccid",
            "sim_tel_number",
            "client_name",
            "sim_cell_operator__id",
            "sim_owner",
            "sim_date",
            "contragent__ca_id",
            "terminal_imei",
            )
    fieldsets = (
            (None, {
                'fields': (
                    'sim_iccid',
                    'sim_tel_number',
#                    'client_name',
                    'sim_cell_operator',
                    'sim_owner',
                    'sim_date',
                    'contragent',
                    "terminal_imei",
                    'itprogrammer',
                )
            }),
    )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'sim_iccid',
                    'sim_tel_number',
#                    'client_name',
                    'sim_cell_operator',
                    'sim_owner',
                    'sim_date',
                    'contragent',
                    "terminal_imei",
                    'itprogrammer'

                )
            })
    )
    raw_id_fields = (
        'contragent',
    )

class DevicesAdmin(admin.ModelAdmin):
    list_display = (
            "device_serial",
            "device_imei",
            "client_name",
            "terminal_date",
            "devices_brand",
            "name_it",
            "sys_mon",
            "contragent",
            'itprogrammer',
            )

    list_filter = (
            "devices_brand",
#            "contragent",
            "terminal_date",
            'itprogrammer',
            )
    search_fields = (
            "device_serial",
            "device_imei",
            "client_name",
            "name_it",
    )
    fieldsets = (
            (None, {
                'fields': (
                    'device_serial',
                    'device_imei',
                    'client_name',
                    'terminal_date',
                    'devices_brand',
#                    'name_it',
                    'sys_mon',
                    'contragent',
                    'itprogrammer',
                )
            }),
    )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'device_serial',
                    'device_imei',
#                    'client_name',
                    'terminal_date',
                    'devices_brand',
#                    'name_it',
                    'sys_mon',
                    'contragent__ca_id',
                    'itprogrammer',
                )
            })
    )
    raw_id_fields = ['contragent']

admin.site.register(Contragents, ContragentsAdmin)
admin.site.register(LoginUsers, LoginUsersAdmin)
admin.site.register(GlobalLogging, GlobalLogAdmin)
admin.site.register(CaObjects, CaObjectsAdmin)
admin.site.register(SimCards, SimCardsAdmin)
admin.site.register(Devices, DevicesAdmin)
