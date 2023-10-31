from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group
from django.forms import ModelForm, ModelChoiceField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            
        )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__( *args, **kwargs)
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Requerido. Ingrese una direccion de correo valida')
    username = forms.CharField(max_length=30, help_text='Requerido. Ingrese un nombre de usuario')
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        
        try:
            account = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"El email {email} ya esta en uso")
    
    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            account = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"El nombre de usuario {username} ya esta en uso")
    
