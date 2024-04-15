from django.db import models

# Create your models here.



class Groups(models.Model):
    name=models.CharField(max_length=100 , verbose_name='Group Name')
    
    def __str__(self):
        return self.name
    

class Students(models.Model):
    username=models.CharField(max_length=20 , verbose_name='Student Name')
    group_id=models.ForeignKey(Groups,on_delete=models.CASCADE,verbose_name='group_id')
    image=models.ImageField(blank=True , upload_to='images' )
    
    def __str__(self):
        return f'{self.username}   |   {self.group_id.name}'
    

class Attendence(models.Model):
    user_id=models.ForeignKey(Students,on_delete=models.CASCADE,verbose_name='user_id')
    date=models.DateField(verbose_name='Added time')
    status=models.BooleanField(default=False,help_text='if it is true , that means user is here')
    
    def __str__(self):
        return f'{self.user_id.username}   |   {self.date}   |   {self.status}'
    
    
    