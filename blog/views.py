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
	contact=ContactUs(request.POST or None)
	Signupform=SignUpForm(request.POST or None)
	Signinform=SignInForm(request.POST or None)
	Changepasswordform=ChangePassword(request.POST or None)
	if request.method=='POST':
		if 'signinsubmit' in request.POST:
			username=request.POST.get("username",False)
			password=request.POST.get("password",False)
			new_user=authenticate(username=username,password=password)
			if new_user is not None:
				if new_user.is_active:
					login(request,new_user)
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
			contact=ContactUs()
		elif 'signupsubmit' in request.POST:
			if Signupform.is_valid():
				username=request.POST.get("username",False)
				password=request.POST.get("password",False)
				email = request.POST.get("email", False)
				user=User.objects.create_user(username,email,password)
				new_user=authenticate(username=username,password=password)
				if new_user is not None:
					if new_user.is_active:
						login(request,new_user)
			Signinform=SignInForm()
			Changepasswordform=ChangePassword()
			contact=ContactUs()
		elif 'passwordchange' in request.POST:
			if Changepasswordform.is_valid():
				old=request.POST.get("old",False)
				new1=request.POST.get("newpass",False)
				new2=request.POST.get("newpass2",False)
				new_user=authenticate(username=request.user,password=old)
				u=User.objects.get(username=request.user)
				if new_user is not None:
					u.set_password(new2)
				u.save()
			Signupform=SignUpForm()
			Signinform=SignInForm()
			contact=ContactUs()

		elif 'logout' in request.POST:
			logout(request)
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
			contact=ContactUs()
		elif 'contactsubmit' in request.POST:
			if contact.is_valid():
				name=contact.cleaned_data.get('name')
				email=contact.cleaned_data.get('email')
				subject=contact.cleaned_data.get('subject')
				message=contact.cleaned_data.get('message')
				send_mail(
 			   		subject,
    				message,
    				email,
    				[settings.EMAIL_HOST_USER],
    				fail_silently=True,
					)
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
			contact=ContactUs()
		else:
			Signinform=SignInForm()
			Signupform=SignUpForm()
			contact=ContactUs()
			Changepasswordform=ChangePassword()
	context={
	'contactus':contact,
	'Signupform':Signupform,
	'Signinform':Signinform,
	'Changepasswordform':Changepasswordform,
	}
	return render(request,"contactus.html",context)
	
def index(request,slug=topics.latest('posted').slug):
	article=get_object_or_404(Topic, slug=slug)
	Signupform=SignUpForm(request.POST or None)
	Signinform=SignInForm(request.POST or None)
	Changepasswordform=ChangePassword(request.POST or None)
	if request.method=='POST':
		if 'signinsubmit' in request.POST:
			username=request.POST.get("username",False)
			password=request.POST.get("password",False)
			new_user=authenticate(username=username,password=password)
			if new_user is not None:
				if new_user.is_active:
					login(request,new_user)
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
		elif 'signupsubmit' in request.POST:
			if Signupform.is_valid():
				username=request.POST.get("username",False)
				password=request.POST.get("password",False)
				email = request.POST.get("email", False)
				user=User.objects.create_user(username,email,password)
				new_user=authenticate(username=username,password=password)
				if new_user is not None:
					if new_user.is_active:
						login(request,new_user)
			Signinform=SignInForm()
			Changepasswordform=ChangePassword()
		elif 'passwordchange' in request.POST:
			if Changepasswordform.is_valid():
				old=request.POST.get("old",False)
				new1=request.POST.get("newpass",False)
				new2=request.POST.get("newpass2",False)
				new_user=authenticate(username=request.user,password=old)
				u=User.objects.get(username=request.user)
				if new_user is not None:
					u.set_password(new2)
				u.save()
			Signupform=SignUpForm()
			Signinform=SignInForm()

		elif 'logout' in request.POST:
			logout(request)
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
		
		else:
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
	context={
	'articles':article,
	'Signupform':Signupform,
	'Signinform':Signinform,
	'Changepasswordform':Changepasswordform,
	}
	return render(request,"index.html",context)

def topic(request,slug=topics.latest('posted').slug):
	article=get_object_or_404(Topic, slug=slug)
	#forms
	Signupform=SignUpForm(request.POST or None)
	Signinform=SignInForm(request.POST or None)
	Changepasswordform=ChangePassword(request.POST or None)
	commentform =CommentForm(request.POST or None,auto_id=False)
	
	#paginator for comments
	comment=Comment.objects.filter(blog=article).order_by('-posted')
	paginator=Paginator(comment,10)
	page2=request.GET.get('page2')
	try:
		comment_page=paginator.page(page2)	
	except PageNotAnInteger:
		comment_page=paginator.page(1)

	#pageinator  for topics	
	paginator=Paginator(topics,10)
	page=request.GET.get('page');
	try:
		article_page=paginator.page(page)
	except PageNotAnInteger:
		article_page=paginator.page(1)

	if request.method=='POST':
		if 'signinsubmit' in request.POST:
			username=request.POST.get("username",False)
			password=request.POST.get("password",False)
			new_user=authenticate(username=username,password=password)
			if new_user is not None:
				if new_user.is_active:
					login(request,new_user)
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
			commentform =CommentForm()
		elif 'signupsubmit' in request.POST:
			if Signupform.is_valid():
				username=request.POST.get("username",False)
				password=request.POST.get("password",False)
				email = request.POST.get("email", False)
				user=User.objects.create_user(username,email,password)
				new_user=authenticate(username=username,password=password)
				if new_user is not None:
					if new_user.is_active:
						login(request,new_user)
			Signinform=SignInForm()
			Changepasswordform=ChangePassword()
			commentform =CommentForm()
		elif 'passwordchange' in request.POST:
			if Changepasswordform.is_valid():
				old=request.POST.get("old",False)
				new1=request.POST.get("newpass",False)
				new2=request.POST.get("newpass2",False)
				new_user=authenticate(username=request.user,password=old)
				u=User.objects.get(username=request.user)
				if new_user is not None:
					u.set_password(new2)
				u.save()	
			Signupform=SignUpForm()
			Signinform=SignInForm()
			commentform =CommentForm()

		elif 'logout' in request.POST:
			logout(request)
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
			commentform =CommentForm()
		elif 'commentsubmit' in request.POST:
			if commentform.is_valid():
				cf=commentform.save(commit=False)
				cf.user=request.user
				cf.blog=Topic(article.pk)
				cf.save()
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
		else:
			Signinform=SignInForm()
			Signupform=SignUpForm()
			Changepasswordform=ChangePassword()
	#comment=Comment.objects.all().order_by('-posted')
	context={
		'articles':article,
		'count':Comment.objects.filter(blog=article).count(),
		'commentform':commentform,
		'Signupform':Signupform,
		'Signinform':Signinform,
		'Changepasswordform':Changepasswordform,
		'article_page':article_page,
		'comment_page':comment_page,
	}
	return render(request,"article.html",context)
	