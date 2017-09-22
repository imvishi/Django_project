from django.conf.urls import url
from .import views
urlpatterns=[
	url(r'^$',views.index,name="home"),
	url(r'^articles/$',views.topic,name="articles"),
	url(r'^contact/$',views.contact,name="contact"),
	url(r'^articles/(?P<slug>[^\.]+)', views.topic, name='topics'),
]
