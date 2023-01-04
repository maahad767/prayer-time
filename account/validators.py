from django.forms import ValidationError


def bsid_validator(value):
    if len(value) != 4:
        raise ValidationError("BSID must be 4 characters long")


def phone_validator(value):
    if len(value) != 14:
        raise ValidationError("Phone must be 14 characters long")
