from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AccountAdmin(UserAdmin):
    # list_display = ('username',)
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account)