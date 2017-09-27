from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^add', views.add),
url(r'^createcar', views.createcar),
url(r'^show/(?P<Id>\d+)', views.show),
url(r'^$', views.index),
]
