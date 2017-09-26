from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^register', views.register),
url(r'^login', views.login),
url(r'^dashboard', views.dashboard),
url(r'^logoff', views.logoff),
url(r'^$', views.index),
]
