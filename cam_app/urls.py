from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('video_feed/', views.video_feed, name='video_feed'),
    path('video_page/', views.video_page, name='video_page'),
]