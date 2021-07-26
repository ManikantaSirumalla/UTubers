from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YTAdmin(admin.ModelAdmin):


    def myphoto(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ('id','myphoto','name', 'subs_count','price','is_featured')
    search_fields = ('name','camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name')



admin.site.register(Youtuber, YTAdmin)