from datetime import datetime
from django.db import models
from django_jalali.db import models as jmodels


class CustomUser(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    username = models.CharField(max_length=256, blank=True, null=True)
    full_name = models.CharField(max_length=256, blank=True, null=True)
    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256,blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    national_code = models.CharField(max_length=10, blank=True, null=True)
    birthday_date = jmodels.jDateField()
    ceremony_datetime = jmodels.jDateTimeField()
    country = models.CharField(max_length=100, default="Iran")

    def save(self, *args, **kwargs):
        if self.gender == "Male":
            self.gender = "M"
        elif self.gender == "Female":
            self.gender = "F"
        super().save(*args, **kwargs)

    def __str__(self):
        gender_display = dict(self.GENDER_CHOICES).get(self.gender, "Unknown")
        return f"Username: {self.username}, Gender: {gender_display}, Full Name: {self.full_name or 'N/A'}"

    def get_first_and_last_name(self):
        if self.full_name:
            parts = self.full_name.split(" ")
            first_name = parts[0] if len(parts) > 0 else ""
            last_name = parts[-1] if len(parts) > 1 else ""
            return {"first_name": first_name, "last_name": last_name}
        return {"first_name": "", "last_name": ""}

    def get_age(self):
        if self.birthday_date:
            today = datetime.now().date()
            age = (
                today.year
                - self.birthday_date.year
                - (
                    (today.month, today.day)
                    < (self.birthday_date.month, self.birthday_date.day)
                )
            )
            return age
        return 0

    def is_birthday(self):
        if self.birthday_date:
            today = datetime.now().date()
            return (
                today.month == self.birthday_date.month
                and today.day == self.birthday_date.day
            )
        return False
