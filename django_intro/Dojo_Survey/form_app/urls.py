from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index),
    path('result/', views.process),
    path('final_result/', views.show)
]