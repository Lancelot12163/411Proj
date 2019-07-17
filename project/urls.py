from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('home', views.base, name='base'),
    path('insert', views.insert, name='insert'),
]
