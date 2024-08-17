from django.contrib import admin
from django.contrib.admin import register
from Users.models import CustomUser


@register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "gender",
        "birthday_date",
    ]
