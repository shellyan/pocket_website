from django.conf.urls import patterns, url

from pocket import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cycle', views.cycle, name='cycle')
)