from django.urls import path
from .views import StudentsAPIView , index , video_feed

urlpatterns = [
    path('', index, name='index'),
    path('video_feed/', video_feed, name='video_feed'),
    path('students/', StudentsAPIView.as_view(),name='Students')
]