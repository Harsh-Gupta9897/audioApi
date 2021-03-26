from django.urls import path
from myaudioapp.views import MyAudioViewSet, PodcastViewSet, AudioBookViewSet, SongViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('myaudio',MyAudioViewSet,basename='myaudio') 
router.register('podcast',PodcastViewSet,basename='podcast') 
router.register('song',SongViewSet,basename='song') 
router.register('audiobook',AudioBookViewSet,basename='audiobook') 



urlpatterns = [
    path('audio/<str:audio_type>/', views.AudioView.as_view(),name="audio"),    
] + router.urls