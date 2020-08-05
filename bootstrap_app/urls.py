from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('timeline', views.timeline),
    path('about_me', views.about)		   
]