from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = '__all__' #__all__ trará todos os campos de User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]