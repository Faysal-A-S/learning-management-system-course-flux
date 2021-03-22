from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    teacher ='teacher'
    student='student'
    premium=models.BooleanField(default=False)
    bio=models.CharField( max_length=100,blank=True)
    user_type=[
        (teacher,'teacher'),
        (student,'student')
    ]
    user_type=models.CharField(max_length=50,choices=user_type,default=student)

    def __str__(self):
        return str(self.user)
    