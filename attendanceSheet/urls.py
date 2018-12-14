from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'collaAdmin'
#name the app

urlpatterns=[
    url(r'^userProfile/$',views.userProfiles_views,name='uerProfile'),
    url(r'^userAttendance/$',views.userAttendance_views,name='userAtd'),
    # url(r'^sign',views.sign,name='sign'),
    path('sign/<int:time>',views.sign,name = 'sign'),
    url(r'^teacherpage',views.teacherpage,name='teacherpage'),
    url(r'^addCourse',views.addCourse,name='addCourse'),
    url(r'^manageCourse',views.manageCourse),
    url(r'^modifyCourse',views.modifyCourse),
]