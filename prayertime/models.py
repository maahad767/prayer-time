from django.db import models

from account.models import OfficeLocation


class PrayerTime(models.Model):
    office_location = models.ForeignKey(
        OfficeLocation,
        on_delete=models.CASCADE,
        verbose_name="Office Location",
        related_name="prayer_times",
    )
    fajr = models.TimeField()
    sunrise = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()
    date = models.DateField()

    class Meta:
        verbose_name = "Prayer Time"
        verbose_name_plural = "Prayer Times"
