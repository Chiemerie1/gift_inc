from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User, Profile, ConfirmImage
from phone_field import PhoneField
from .models import PhoneField
from .import models



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = models.PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        model = User
        fields = ("username", "first_name", 
                    "last_name", "email", "phone",
                    "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]

        if commit:
            user.save()

        return user


class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("phone","account_details",
                    "user_id")
        exclude = ("user_id",)

class ConfirmForm(forms.ModelForm):
    upload = forms.FileField()
    class Meta:
        model = ConfirmImage
        fields = ("upload",)