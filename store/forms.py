from django import forms
from store.models import LoginModel

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'
        labels = {
            "name": "Name",
            "email": "Email",
            "password": "Password"
        }