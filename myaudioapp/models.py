from django.db import models

# Create your models here.
class MyAudio(models.Model):
    AUDIO_CHOICES = (
        ('Song','Song'),
        ('Podcast','Podcast'),
        ('Audiobook','Audiobook'),
    )

    audio_type = models.CharField(choices=AUDIO_CHOICES,max_length=10)


class Song(MyAudio):
    name_of_the_song = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)


class Podcast(MyAudio):
    name_of_the_podcast = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)   
    participants = models.CharField(max_length=1000,null=True,blank=True)

class Audiobook(MyAudio):
    title_of_the_audiobook = models.CharField(max_length=100)
    author_of_the_title = models.CharField(max_length=100) 
    narrator  = models.CharField(max_length=100) 
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)



class Audio(models.Model):
    AUDIO_CHOICES = (
        ('Song','Song'),
        ('Podcast','Podcast'),
        ('Audiobook','Audiobook'),
    )

    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    audio_type = models.CharField(choices=AUDIO_CHOICES,max_length=10)

    author_of_the_title = models.CharField(max_length=100,blank=True,null=True) 
    narrator  = models.CharField(max_length=100,blank=True,null=True) 
    participants = models.CharField(max_length=1000,null=True,blank=True)
    host = models.CharField(max_length=100)   