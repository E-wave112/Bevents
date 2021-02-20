from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import AuthUser


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class AuthUserCreationForm(UserCreationForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('email','username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AuthUserChangeForm(UserChangeForm):

    class Meta:
        model = AuthUser
        fields = ('email','username')