from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import AuthUser


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class AuthUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('email','username','password1','password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AuthUserChangeForm(UserChangeForm):

    class Meta:
        model = AuthUser
        fields = ('email','username')