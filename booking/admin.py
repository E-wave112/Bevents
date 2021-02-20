from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuthUserCreationForm, AuthUserChangeForm
from .models import AuthUser,OrganizerProfile,EventUserProfile

# Register your models here.
class AuthUserAdmin(UserAdmin):
    add_form = AuthUserCreationForm
    form = AuthUserChangeForm
    model = AuthUser
    list_display = ('email', 'username', 'is_staff', 'is_active',)
    list_filter = ('email', 'username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','username','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','username',)
    ordering = ('email',)


admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(OrganizerProfile)
admin.site.register(EventUserProfile)

