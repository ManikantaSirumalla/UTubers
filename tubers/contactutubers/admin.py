from django.contrib import admin
from .models import Contactutubers
# Register your models here.


class contactadmin(admin.ModelAdmin):

        list_display = ('full_name', 'subject')
        search_fields = ('subject','full_name')

        list_display_links = ('full_name','subject')

admin.site.register(Contactutubers,contactadmin)