from django.contrib import admin

# Register your models here.
from .models import Music, AccessLogSearch


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist', "duration", "released_data", "url")


@admin.register(AccessLogSearch)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('access_time', 'music_name', 'from_db', "user_ip")


# admin.site.register(Music, MusicAdmin)