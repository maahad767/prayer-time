from django.forms import ValidationError


import re


def bsid_validator(value):
    result = re.match(r"^BS\d{4}$", value)
    if result is None:
        raise ValidationError("BSID must be valid BSID(BSXXXX)")


def phone_validator(value):
    result = re.match(r"^(?:\+?88)?01?\d{9}$", value)
    if result is None:
        raise ValidationError("Phone must be valid Bangladeshi phone number")
