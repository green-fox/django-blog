from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text_field = models.TextField(max_length=20000)

#class Picture(models.Model):
    

class Video(models.Model):
    YOUTUBE = 'YT'
    DAILYMOTION = 'DM'
    VIMEO = 'VM'
    VIDEO_PLAYER_CHOICES= (
        (YOUTUBE, 'youtube'),
        (DAILYMOTION, 'dailymotion'),
        (VIMEO,'vimeo'),
    )
    video_player = models.CharField(max_length = 2,
                    choices = VIDEO_PLAYER_CHOICES,
                    default = YOUTUBE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

#class Concert(models.Model):
