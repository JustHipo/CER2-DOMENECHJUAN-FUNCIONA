from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Comunicado
from django.contrib.auth.models import Group
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username','email', 'role',"is_staff", "is_active", )
    list_filter = ('username','email', 'role', "is_staff", "is_active")
    fieldsets = (
        (None, {'fields': ('username', 'email','password', 'role', 'is_staff', 'is_active', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password1', 'password2','role', 'is_staff', 'is_active','user_permissions')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Comunicado)
