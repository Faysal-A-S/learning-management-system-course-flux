from django.shortcuts import render
from .models import Institute,Department,Course,Lecture,Subscribe
import random
# Create your views here.
def department(request,id):
    department=Department.objects.filter(inst_name =id)
    university=Institute.objects.get(pk=id)
    institute=Institute.objects.all()
    
    context={
        'departments':department,
        'university':university,
        'institute':institute
    }
    return render(request,'university/university.html',context)

def courses(request,id):
    course=Course.objects.filter(dept=id)
    institute=Institute.objects.all()
    
    context={
        'course':course,
        'institute':institute
    }
    return render(request,'university/course.html',context)
def lectures(request,id) :
    lecture=Lecture.objects.filter(course=id).order_by('id')
    institute=Institute.objects.all()

    if request.user.is_authenticated:
        subscribe=Subscribe.objects.filter(user_id=request.user,course_id=id)
        if subscribe:
            context={
                'lectures':lecture,
                'subscribe':subscribe,
                'institute':institute
            }
        else:
            subscribe.subscribed=False    
            context={
                 'lectures':lecture,
                  'subscribe':subscribe.subscribed,
                  'institute':institute
                 }
    else:
        subscribe=Subscribe.objects.filter(user_id=6,course_id=id)
        if subscribe:
            context={
                'lectures':lecture,
                'subscribe':subscribe,
                'institute':institute
            }
        else:
            subscribe.subscribed=False    
            context={
                 'lectures':lecture,
                  'subscribe':subscribe.subscribed,
                  'institute':institute
                 }             
    return render(request,'university/lecture.html',context)

def video(request,number):
    
    video=Lecture.objects.filter(lecture_id=number)
    institute=Institute.objects.all()
    for vid in video:

        lecture=Lecture.objects.filter(course=vid.course).order_by('id')
        
        if request.user.is_authenticated:
            subscribe=Subscribe.objects.filter(user_id=request.user,course_id=vid.course)
            logo='paid.jpg'
            if subscribe:
                
                context={
                     'video':video,
                     'lectures':lecture,
                     'subscribe':subscribe,
                     'logo':logo,
                     'institute':institute
                }
          
            else:
                subscribe.subscribed=False
                context={
                    'video':video,
                     'lectures':lecture,
                     'subscribe':subscribe.subscribed,
                     'logo':logo,
                     'institute':institute
                }
        else:
            subscribe=Subscribe.objects.filter(user_id=6,course_id=vid.course)
            logo='paid.jpg'
            if subscribe:
                
                context={
                     'video':video,
                     'lectures':lecture,
                     'subscribe':subscribe,
                     'logo':logo,
                     'institute':institute
                }
          
            else:
                subscribe.subscribed=False
                context={
                    'video':video,
                     'lectures':lecture,
                     'subscribe':subscribe.subscribed,
                     'logo':logo,
                     'institute':institute
                }

               
       
        
        return render(request,'university/video.html',context)  



def aboutus(request):
    institute=Institute.objects.all()
    context={
        'institute':institute
    }
    return render(request,'university/aboutus.html',context)
        

