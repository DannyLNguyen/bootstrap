from django.urls import path     
from . import views
urlpatterns = [
    path('', views.welcome),
    path('about_me', views.about)		   
]