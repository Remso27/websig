from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
from . import views


app_name = 'RestotelMap'

urlpatterns = [
    path('', views.index, name='index'),
     path('search/', search_view, name='search_view'),
]