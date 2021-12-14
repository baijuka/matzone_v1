from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
    )

admin.site.register(Contact, ContactAdmin)
