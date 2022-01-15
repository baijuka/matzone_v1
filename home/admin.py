from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'message',
        'date_sent',
    )
    ordering = ('-date_sent',)

admin.site.register(Contact, ContactAdmin)
