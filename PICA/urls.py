"""
PICA URL Configuration
"""
from django.urls import path
from django.views.generic import RedirectView
from main import views

urlpatterns = [

    path(r'', views.home, name='home'),

    path(r'calls', views.calls, name='calls'),

    path(r'organization', views.organization, name='organization'),

    path(r'gallery', RedirectView.as_view(url='/photos'), name='gallery'),

    path(r'posters', views.posters, name='posters'),

    path(r'photos', views.photos, name='photos'),

    path(r'presentations', views.presentations, name='presentations'),

]
