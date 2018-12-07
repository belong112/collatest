from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/') #remeber the slash at the very front
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',locals())

def login_views(request,timecode):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user=form.get_user()
            login(request,user)
            if user is not None:
                if request.user.is_superuser:
                    return redirect('/collaAdmin/teacherpage')
                else:
                    if timecode==0:
                        return redirect('/collaAdmin/userProfile/')
                    else: 
                        return redirect('sign',time = timecode)
    else:
        form = AuthenticationForm()
    
    return render(request,'accounts/login.html',locals())


def logout_views(request):
    logout(request)
    return redirect('/')
