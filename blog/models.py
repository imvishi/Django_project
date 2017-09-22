# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
	title=models.CharField(max_length=100,blank=False,null=False,unique=True)
	body=models.TextField()
	slug=models.SlugField(max_length=100,unique=True)
	posted=models.DateField(auto_now_add=True)
	def __unicode__(self):
		return  self.title
	def get_absolute_url(self):
		return reverse('topics',kwargs={"slug": self.slug})

class Comment(models.Model):
	comment=models.CharField(max_length=200)
	posted=models.DateTimeField(auto_now_add=True)
	blog=models.ForeignKey(Topic,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __unicode__(self):
		return self.comment