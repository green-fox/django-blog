from django.contrib import admin

# Register your models here.
from django.contrib import admin
from music_band_blog.models import Video

class VideoAdmin(admin.ModelAdmin):
    fields = ['title','video_player' ]
    list_display = ('title','video_player','pub_date','updated')
admin.site.register(Video,VideoAdmin)
