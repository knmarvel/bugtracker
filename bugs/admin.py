from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bugs.models import MyUser, Ticket


# help in this section is from janell.huyck and 
# https://testdriven.io/blog/django-custom-user-model/
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'display_name', 'is_staff', 'is_active',)
    list_filter = ('username', 'display_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'display_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )


class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Ticket, TicketAdmin)