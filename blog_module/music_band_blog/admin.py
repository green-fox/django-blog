from django.contrib import admin

# Register your models here.
from django.contrib import admin
from music_band_blog.models import Video

class VideoAdmin(admin.ModelAdmin):
    fields = ['title','type','pub_date','updated' ]

admin.site.register(Video,VideoAdmin)
