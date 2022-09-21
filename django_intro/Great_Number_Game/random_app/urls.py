from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('process', views.random_number),
    path('path', views.redirect_route),
    path('again', views.again),
    ]