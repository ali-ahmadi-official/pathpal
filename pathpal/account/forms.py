from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import User

class CustomeUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'password', 'phone_number']
    
    password = forms.CharField(widget=forms.PasswordInput)

class PhoneLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=10, min_length=10, required=True, label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput, required=False, label="Password")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone_number

    def authenticate(self):
        phone_number = self.cleaned_data.get("phone_number")
        password = self.cleaned_data.get("password")
        User = get_user_model()

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise ValidationError("کاربری با این شماره یافت نشد.")

        if password:
            user = authenticate(request=None, username=phone_number, password=password)
            if user is None:
                raise ValidationError("رمز عبور اشتباه است.")
        
        return user
