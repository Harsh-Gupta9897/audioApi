from django.shortcuts import render
from myaudioapp.models import MyAudio,Song,Podcast,Audiobook,Audio
from myaudioapp.serializers import MyAudioSerializer,SongSerializer,PodcastSerializer,AudiobookSerializer,Podcast1Serializer , AudioSerializers
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.
class MyAudioViewSet(viewsets.ModelViewSet):
    queryset = MyAudio.objects.all()
    serializer_class = MyAudioSerializer 

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer 

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer 

class AudioBookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer 


class AudioView(APIView):
    def post(self,request,audio_type,pk=None):
        if audio_type == "podcast":
            serializer = Podcast1Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)

        if audio_type == "song":
            serializer = AudioSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=200)
        
        if audio_type == "audiobook":
            serializer = Podcast1Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)


        return Response("audio_type_not exists") 

               

    def get(self,request,audio_type,pk=None):
        if audio_type=="podcast":
            queryset = Audio.objects.filter(audio_type="Podcast")
            serializer = Podcast1Serializer(queryset, many=True)
            return Response(serializer.data,status=200)
        if audio_type=="song":
            queryset = Audio.objects.filter(audio_type="Song")
            serializer = AudioSerializers(queryset, many=True)
            return Response(serializer.data,status=200)
        
        return Response("failed")

    def update(self,request,audio_type,pk):
        return Response("coming soon")