from django.shortcuts import render


from django.http import StreamingHttpResponse
from .camera import VideoCamera

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from .models import Students , Attendence
from .serializers import StudentsSerializers , AttendenceSerializers 

# a=Students.subjects.all()
# print(a)

class StudentsAPIView(APIView):
    serializer_class=StudentsSerializers
    permission_classes=(AllowAny,)
    def get(self,request):
        students=Students.objects.all()
        print(students)
        serializer=StudentsSerializers(students,many=True)
        return Response(data=serializer.data)

class AttendenceAPIView(APIView):
    serializer_class=AttendenceSerializers
    permission_classes=(AllowAny,)
    def get(self,request):
        students=Students.objects.all()
        print(students)
        attends=Attendence.objects.filter(user_id__in=students)
        print(students)
        print(attends)
        serializer=AttendenceSerializers(attends,many=True)
        return Response(data=serializer.data)




def index(request):
    return render(request, 'index.html')

def video_feed(request):
    return StreamingHttpResponse(VideoCamera().generate_frames_and_check_faces(), content_type='multipart/x-mixed-replace; boundary=frame')