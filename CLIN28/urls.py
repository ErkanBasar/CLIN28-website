"""
CLIN28 URL Configuration
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^$', views.Home.as_view(), name='home'),

	url(r'^participants$', login_required(views.DisplayParticipants.as_view()), name='display_participants'),

    url(r'^dates$', views.Dates.as_view(), name='dates'),

    url(r'^call_for_papers$', views.Calls.as_view(), name='calls'),

    # Not in use;
    url(r'^check_email/$', views.check_email, name='check_email'),

#    url(r'^program$', views.ModifyProgram.as_view(), name='modify_program')

]
