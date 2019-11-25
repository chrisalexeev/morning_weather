from django import forms
from localflavor.us.forms import USZipCodeField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password1', 'password2']

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class ProfileForm(forms.ModelForm):
    zipcode = USZipCodeField()

    class Meta:
        model = Profile
        fields = ['zipcode']
"""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
"""