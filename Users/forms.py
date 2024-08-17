from django import forms
from django.core.exceptions import ValidationError
from django_jalali.forms import jDateField, jDateTimeField
from Users.models import CustomUser  # Adjust the import based on your file structure

class CustomUserForm(forms.ModelForm):
    username = forms.CharField(max_length=256, required=False)
    full_name = forms.CharField(max_length=256, required=False)
    gender = forms.ChoiceField(choices=[("M", "Male"), ("F", "Female")], required=True)
    national_code = forms.CharField(max_length=10, required=False)
    birthday_date = jDateField(required=True)
    ceremony_datetime = jDateTimeField(required=True)
    country = forms.CharField(max_length=100, initial="Iran", required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'gender', 'national_code', 'birthday_date', 'ceremony_datetime', 'country']

    def clean_national_code(self):
        national_code = self.cleaned_data.get("national_code")
        if national_code and len(national_code) != 10:
            raise ValidationError("National code must be exactly 10 characters long.")
        return national_code

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if full_name:
            parts = full_name.split()
            if len(parts) != 2:
                raise ValidationError(
                    "Full name must include both first name and last name."
                )

            first_name, last_name = parts
            if not (first_name.istitle() and last_name.istitle()):
                raise ValidationError(
                    "Both first name and last name must be capitalized."
                )

        return full_name
