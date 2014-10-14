from django.db import models

# Create your models here.


#class Article(models.Model):
    title = models.CharField(max_length=200)

#class Picture(models.Model):
    

class Video(models.Model):
    YOUTUBE = 'YOUTUBE'
    DAILYMOTION = 'DAILYMOTION'
    VIMEO = 'VIMEO'
    VIDEO_PLAYER_CHOICES= (
        (YOUTUBE, 'youtube'),
        (DAILYMOTION, 'dailymotion'),
        (VIMEO,'vimeo'),
    )
    video_player = (max_length = 1,
                    choices = VIDEO_PLAYER_CHOICES,
                    default = YOUTUBE)
    title = models.CharField(max_length=200)

#class Concert(models.Model):
