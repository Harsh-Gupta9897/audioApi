from django.contrib import admin
from myaudioapp.models import Audiobook,Podcast,Song, MyAudio,Audio

# Register your models here.

class MyAudioAdmin(admin.ModelAdmin):
    list_display  = ('id','audio_type')

admin.site.register(MyAudio, MyAudioAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display  = ('id','audio_type','name_of_the_song','duration')
admin.site.register(Song,SongAdmin)
admin.site.register(Podcast)
admin.site.register(Audiobook)
admin.site.register(Audio)