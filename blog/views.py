# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


topics=Topic.objects.all().order_by('posted')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('')

def contact(request):
	return render(request,"contactus.html",{})
	
def index(request):
	return render(request,"index.html",{})

def topic(request):
	return render(request,"article.html",{})
	