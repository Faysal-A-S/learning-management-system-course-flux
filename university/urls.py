from django.urls import path,re_path

from . import views


urlpatterns = [
    
    path('department/<str:id>',views.department,name='department'),
     path('course/<str:id>',views.courses, name='course'),
     path('lecture/<str:id>',views.lectures, name='lecture'),
     path('video/<str:number>',views.video,name='video'),
     
 

]
