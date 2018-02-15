"""
CLIN28 URL Configuration
"""
from django.conf.urls import url
from django.views.generic import RedirectView
from main import views

urlpatterns = [

    url(r'^$', views.home, name='home'),

    url(r'^dates$', views.dates, name='dates'),

    url(r'^calls$', views.calls, name='calls'),

    url(r'^shared_task$', views.shared_task, name='shared_task'),

    url(r'^stil_thesis_prize$', views.thesis_prize, name='stil_thesis_prize'),

    url(r'^gallery$', RedirectView.as_view(url='/photos'), name='gallery'),

    url(r'^posters$', views.posters, name='posters'),

    url(r'^photos$', views.photos, name='photos'),

    url(r'^presentations$', views.presentations, name='presentations'),

]
