from django.contrib import admin
from .models import HireYoutubers
# Register your models here.


class hireadmin(admin.ModelAdmin):

        list_display = ('user_id', 'first_name', 'email', 'utuber_name')

        search_fields = ('name', 'utuber_name')
        list_filter = ('city', 'state')
        list_display_links = ('user_id', 'first_name')

admin.site.register(HireYoutubers,hireadmin)