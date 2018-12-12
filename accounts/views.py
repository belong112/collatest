from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from attendanceSheet.models import attendanceSheet,date_course
# Create your views here.

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            form.save()
            #create new attendance record for new user
            courseLst=date_course.objects.all()
            user=User.objects.get(username=username)
            for course in courseLst:
                attendanceSheet.objects.create(user=user,course=course)
            
            #return HttpResponse(user)
            return redirect('/collaAdmin/teacherpage ') #remeber the slash at the very front
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',locals())

def login_views(request,timecode):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user=form.get_user()
            login(request,user)
            if request.user.is_authenticated:
                return redirect('/collaAdmin/teacherpage')
            else:
                return HttpResponse("student page here")
    else:
        form=AuthenticationForm
    return render(request,'accounts/login.html',locals())

def logout_views(request):
    logout(request)
    return redirect('/')
