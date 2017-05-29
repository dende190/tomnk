from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^historia$', views.history, name='history'),
    url(r'^contacto$', views.contact, name='contact'),
    url(r'^fotos$', views.pictures, name='pictures'),
    url(r'^bandas/(?P<pk>[0-9]+)/$', views.info_bandas, name='info_bandas'),
]