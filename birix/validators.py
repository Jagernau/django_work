from os import walk
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_sim_tel_number(value):
    if value is not None and (len(value) != 11 or '+' in value or ' ' in value):
        raise ValidationError(
            _('Неверно указан номер. Убедитесь, что номер содержит 11 символов, не содержит символ "+", и не содержит пробелов.'),
            code='invalid_sim_tel_number'
        )

def validate_sim_iccid_number(value):
    if len(value) > 19:
        raise ValidationError('Длина iccid сим-карты не должна превышать 19 символов.')

def validate_password(value):
    if not re.search(r'[A-Z]', value):
        raise ValidationError(
            _('Пароль должен содержать хотя бы одну заглавную букву.'),
            code='invalid_password_capital_letter'
            )
    if not re.search(r'[\W_]', value):
        raise ValidationError(
            _('Пароль должен содержать хотя бы один спец. символ.'),
            code='invalid_password_special_simbol'
            )
    if not re.search(r'[0-9]',value):
        raise ValidationError(
            _('Пароль должен содержать хотя бы одну цифру.'),
            code='invalid_password_number'
            )
def validate_login(value):
    if '.' not in value or '@' not in value:
        raise ValidationError(
            _('Неверный формат email.'),
            code='invalid_email'
            )

