from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.decorators import register

from account.models import OfficeLocation, User
from prayertime.models import PrayerTime


@register(OfficeLocation)
class OfficeLocationAdmin(admin.ModelAdmin):
    list_display = ("branch", "floor")
    search_fields = ("branch", "floor")


@register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "bsid", "phone", "office_location")
    search_fields = ("username", "bsid", "phone", "office_location")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("bsid", "phone", "office_location")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


@register(PrayerTime)
class PrayerTimeAdmin(admin.ModelAdmin):
    pass
