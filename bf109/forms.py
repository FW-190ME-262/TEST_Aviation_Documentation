from django import forms
from django_recaptcha.fields import ReCaptchaField

from .models import Object,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class PhoneLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)



class Object(forms.ModelForm):
    class Meta:
        model = Object
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    recaptcha = ReCaptchaField()
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    recaptcha = ReCaptchaField()
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'recaptcha']
