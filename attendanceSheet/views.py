from django.shortcuts import render,redirect
from . models import userProfile,attendanceSheet,date_course
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def userProfiles_views(request):
    allUsers=userProfile.objects.all()

    if (request.method=="hold on a second"):
        #do something searched
        finalPresent=allUsers[0]
    else:
        finalPresent=allUsers

    context = {'finalPresent':finalPresent}
    return render(request,'userProfiles_tepl.html',context=context)

def userAttendance_views(request):
    if request.method=='POST':
        #do some shit
        return HttpResponse('fuck my life')
    else:
        userLst=User.objects.all()

        courseLst=date_course.objects.all()
        atdDict=dict()

        for user in userLst:
            atdDict[user.username]=[]
            for course in courseLst:
                atdDict[user.username].append(user.attendanceSheet.order_by('-id').get(course=course).status())
        
    return render(request,'userAtd_tepl.html',locals())

def sign(request):
    if request.user.is_authenticated:
        username=request.user.username
        currentUser=User.objects.get(username=username)
        today=datetime.now().strftime('%Y/%m/%d')
        currenCourse=date_course.objects.get(date=today)

        attendanceSheet.objects.filter(user=currentUser,course=currenCourse).update(presence=True,absence=False)
        return HttpResponse('succesfully signUp')
        
    return redirect('/accounts/login')

def teacherpage(request):
    return render(request,'teacherpage.html')

def addCourse(request):
    if request.method=="POST":
        courseDate=request.POST['course_date']
        courseName=request.POST['course_name']
        courseDescription=request.POST['course_description']
        date_course.objects.create(date=courseDate,course_name=courseName,memo=courseDescription)

        #幫固有的使用者創建新課堂的出席紀錄
        userLst=User.objects.all()
        newCourse=date_course.objects.get(course_name=courseName)
        for user in userLst:
            attendanceSheet.objects.create(user=user,course=newCourse)
        return redirect('/collaAdmin/userAttendance')
    else:
       return render(request,'addCourse.html',locals())

def manageCourse(request):
    return HttpResponse('manageCourse')