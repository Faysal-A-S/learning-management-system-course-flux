from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
class Institute(models.Model):
    name=models.CharField( max_length=50)
    slug=models.SlugField(null=True,blank=True)
    def  __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)    
    


class Department(models.Model):
    name=models.CharField(max_length=50)
    inst_name  = models.ForeignKey(Institute, on_delete=models.CASCADE,related_name='depts')
    slug=models.SlugField(null=True,blank=True)

    def  __str__(self):
        return str(self.inst_name )+ str(": ")+str(self.name)

       

class Course(models.Model):
    course_code=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    slug=models.SlugField(null=True,blank=True)
    dept=models.ForeignKey(Department,  on_delete=models.CASCADE,related_name='courses')
    image=models.ImageField( default='default.png'  ,null=True,blank=True)
    description=models.CharField( max_length=50,null=True,blank=True)
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    def __str__(self):
        return str(self.dept)+str(": ")+str(self.name)
        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.course_code)
        super().save(*args,**kwargs)


class Lecture(models.Model):
    lecture_name=models.CharField( max_length=50)  
    dept=models.ForeignKey(Department,  on_delete=models.CASCADE) 
    created_bt=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now_add=True) 
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    slug=models.SlugField(null=True,blank=True)
    video=models.FileField(default='default.png', blank=True,null=True)
    notes=models.FileField(default='default.png',  blank=True,null=True)
    premium=models.BooleanField(default=True)
    def __str__(self):
        return str(self.course)+str(": ")+str(self.lecture_name)
    

class Subscribe(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user_id)+str('-')+str(self.course_id)
    

class Payment(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE) 
    sub_id=models.ForeignKey(Subscribe, on_delete=models.CASCADE) 
    paid=models.BooleanField(default=False)      