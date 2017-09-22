# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Topic,Comment
# Register your models here.
class BlogTopic(admin.ModelAdmin):
	list_display=['title','posted','body','slug'];
	prepopulated_fields = {'slug': ('title',)};
admin.site.register(Topic,BlogTopic)

class BlogComment(admin.ModelAdmin):
	list_display=['comment','posted','blog','user'];
admin.site.register(Comment,BlogComment)