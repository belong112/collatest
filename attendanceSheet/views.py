from django.shortcuts import render,redirect
from . models import userProfile,attendanceSheet,date_course,leaveApplication
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from datetime import date

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
    userLst=User.objects.all()
    if request.method=='POST':
        if request.POST['targetUser']!='':
            userLst=User.objects.filter(username__contains=request.POST['targetUser'])

    courseLst=date_course.objects.order_by('date')
    atdDict=dict()

    for user in userLst:
        atdDict[user.username]=[]
        for course in courseLst:
            atdDict[user.username].append(user.attendanceSheet.order_by('-id').get(course=course).status())
    
    return render(request,'userAtd_tepl.html',locals())

def sign(request,time):
    time_copy = time
    c = time_copy%10
    time_copy /= 10
    s = time_copy%100
    m = time_copy/100
    m2 = datetime.now().strftime("%M")
    s2 = datetime.now().strftime("%S")
    delta_s = (int(m2)-m)*60 + int(s2)-s+18

    if delta_s > 30:
        return HttpResponse('u are yoo late hahaha')
    else:
        if request.user.is_authenticated:
            username=request.user.username
            currentUser=User.objects.get(username=username)
            today=datetime.now().strftime('%Y/%m/%d')
            currenCourse=date_course.objects.get(course_name = 'course'+str(c))

            attendanceSheet.objects.filter(user=currentUser,course=currenCourse).update(presence=True,absence=False)
            return HttpResponse('succesfully signUp')
            
        return redirect('/accounts/login/'+str(time))
    

def teacherpage(request):
    return render(request,'teacherpage.html')

def addCourse(request):
    if request.method=="POST":
        courseDate=request.POST['course_date']
        courseName=request.POST['course_name']
        courseDescription=request.POST['course_description']
        date_course.objects.create(date=courseDate,course_name=courseName,memo=courseDescription,is_rollcallNow=False)

        #幫固有的使用者創建新課堂的出席紀錄
        userLst=User.objects.all()
        newCourse=date_course.objects.get(course_name=courseName)
        for user in userLst:
            attendanceSheet.objects.create(user=user,course=newCourse)
        return redirect('/collaAdmin/userAttendance')
    else:
       return render(request,'addCourse.html',locals())

def manageCourse(request):
    courseLst=date_course.objects.order_by('date')
    return render(request,'manageCourse.html',locals())

def modifyCourse(request):
    if request.method=='GET':
        targetName=request.GET['targetName']
        targetDate=date_course.objects.get(course_name=targetName).date
        targetMemo=date_course.objects.get(course_name=targetName).memo
        return render(request,'modifyCourse.html',locals())
        
    elif request.method=='POST':
        originName=request.POST['targetCourse']
        newName=request.POST['course_name']
        newDate=request.POST['course_date']
        newMemo=request.POST['course_description']
        targetCourse=date_course.objects.filter(course_name=originName)
        if newMemo=='':
            newMemo=date_course.objects.get(course_name=originName).memo
        test=newName+newDate+newMemo+originName

        targetCourse.update(date=newDate)
        targetCourse.update(memo=newMemo)
        targetCourse.update(course_name=newName)
        return redirect('/collaAdmin/manageCourse')

def studentpage(request):
    return render(request,'studentpage.html',locals())

def leaveApplication_view(request):

    return HttpResponse('leave application')

def personalAtd(request):
    querySet=date_course.objects.order_by('date')
    tableRow=[]
    temp=[]
    if request.method=='POST':
        if request.POST['targetCourse']!='':
            querySet=date_course.objects.filter(course_name__contains=request.POST['targetCourse'])

    for course in querySet:
        temp.append(course.course_name)
        temp.append(course.date)
        temp.append(course.memo)
        temp.append(attendanceSheet.objects.get(user=request.user,course=course).status())
        tableRow.append(temp)
        temp=[]

    return render(request, 'personalAtd.html',locals())