from rest_framework import serializers
from .models import Groups , Students , Attendence

class GroupsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Groups
        fields='name'
    

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('username','group_id','image')
    
class AttendenceSerializers(serializers.ModelSerializer):
    class Meta:
        model=Attendence
        fields=('user_id','date','status')
    
 
