"""
CLIN28 URL Configuration
"""
from django.conf.urls import url
from main import views

urlpatterns = [

    url(r'^$', views.home, name='home'),

    url(r'^dates$', views.dates, name='dates'),

    url(r'^calls$', views.calls, name='calls'),

    url(r'^shared_task$', views.shared_task, name='shared_task'),

    url(r'^stil_thesis_prize$', views.thesis_prize, name='stil_thesis_prize'),

]
