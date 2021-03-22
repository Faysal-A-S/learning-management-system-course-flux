from django.contrib import admin
from .models import Institute,Department,Course,Lecture,Subscribe



class CourseAdmin(admin.ModelAdmin):
    list_display =('courses','description','dept')
    def courses(self,obj):
        return obj.name
     
    def get_queryset(self,request):
        queryset=super(CourseAdmin,self).get_queryset(request)
        queryset=queryset.order_by('dept')
        return queryset      
class DepartmentAdmin(admin.ModelAdmin):
    list_display =('name','inst_name')
    def get_queryset(self,request):
        queryset=super(DepartmentAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-inst_name')
        return queryset 

class LectureAdmin(admin.ModelAdmin):
    list_display=('lecture_name','dept','course','created_at')
    def get_queryset(self,request):
        queryset=super(LectureAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-course','lecture_name')
        return queryset 
class SubscribeAdmin(admin.ModelAdmin):
    list_display=('user_id','course_id','subscribed') 
    def get_queryset(self,request):
        queryset=super(SubscribeAdmin,self).get_queryset(request)
        queryset=queryset.order_by('user_id')
        return queryset 












# Register your models here.
admin.site.register(Institute)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lecture,LectureAdmin)
admin.site.register(Subscribe,SubscribeAdmin)
