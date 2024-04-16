from django.urls import path
from .views import StudentsAPIView , AttendenceAPIView , index , video_feed

urlpatterns = [
    path('', index, name='index'),
    path('video_feed/', video_feed, name='video_feed'),
    path('students/', StudentsAPIView.as_view(),name='Students'),
    path('attends/', AttendenceAPIView.as_view(),name='Attends')
]