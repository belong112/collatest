from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth,contenttypes


def homepage(request):
		return render (request, "homepage.html")
	
def rollcall(request):
	return render (request, "rollcall.html")	



