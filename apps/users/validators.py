import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

phone_regex = re.compile(r"^\+\d{7,16}$")


def phone_validator(value):
    if not phone_regex.match(value):
        raise ValidationError(_("Phone is not valid, it must start with country code example. +20"))
