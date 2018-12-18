from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth,contenttypes
from attendanceSheet.models import date_course

def homepage(request):
		return render (request, "homepage.html")
	
def rollcall(request):
	courseLst = date_course.objects.order_by('date')
	return render (request, "rollcall.html",locals())



