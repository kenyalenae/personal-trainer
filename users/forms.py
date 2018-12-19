from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# form for user to update their email and username
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# form for user to update all other profile details
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'age', 'city', 'phone', 'height', 'weight', 'membership', 'notes', 'image']
        widgets = {
            'email': Textarea(attrs={'cols': 1, 'rows': 2}),
        }
