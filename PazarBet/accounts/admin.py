from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from PazarBet.accounts.forms import UserCreateForm, UserEditForm

UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    # add_form = UserCreateForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'balance', 'gender', 'is_staff')

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'email',
            'gender',
            'balance',
        )}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )