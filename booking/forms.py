from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AuthUser

class AuthUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = AuthUser
        fields = ('email','username')


class AuthUserChangeForm(UserChangeForm):

    class Meta:
        model = AuthUser
        fields = ('email','username')