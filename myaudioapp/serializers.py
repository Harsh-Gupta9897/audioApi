from rest_framework import serializers
from myaudioapp.models import MyAudio,Song,Podcast,Audiobook,Audio
from utilities.helpers import (get_instances_from_list_of_string)
from rest_framework.response import Response

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id','name_of_the_song','duration']

class PodcastSerializer(serializers.ModelSerializer):

      
    class Meta:
        model = Podcast
        fields = ['id','name_of_the_podcast','duration','host','participants']

class AudiobookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Audiobook
        fields = ['id','title_of_the_audiobook','author_of_the_title','narrator','duration']

class MyAudioSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = MyAudio
        fields = ['id','audio_type','song','podcast','audiobook']

    def create(self, validated_data):

        song_data = validated_data.pop("song")
        podcast_data = validated_data.pop("podcast")
        audiobook_data = validated_data.pop("audiobook")
        audio_type = validated_data.get('audio_type','')
        
        song = Song.objects.create(audio_type=audio_type, **song_data)
        podcast = Podcast.objects.create(audio_type=audio_type, **podcast_data)
        audiobook = Audiobook.objects.create(audio_type=audio_type, **audiobook_data)

        return song
     


#harsh
class AudioSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = Audio
        fields = ['id','name','duration','uploaded_time']


class Podcast1Serializer(AudioSerializers):
    host = serializers.CharField(required=True)
    participants = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    
    class Meta:
        model = Audio
        fields = ['id','name','duration','uploaded_time','host','participants']

