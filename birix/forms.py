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


import re

class SmsForm(forms.Form):
    phone_numbers = forms.CharField(
        label='Номера телефонов',
        widget=forms.Textarea,
        help_text='Номера через запятую\nCтрого 79040000000'
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea
    )

    def clean_phone_numbers(self):
        data = self.cleaned_data['phone_numbers']
        # Разделение номеров по запятым, пробелам или переносам строк
        numbers = re.split(r'[, \n]+', data)
        # Очистка и проверка номеров
        cleaned_numbers = [num.strip() for num in numbers if num.strip()]
        if not cleaned_numbers:
            raise forms.ValidationError('Введите хотя бы один номер телефона.')
        return cleaned_numbers
