from django.contrib import admin 
from django.urls import path 
from .views import helloword, index
  
urlpatterns = [ 
    path('sayhello', helloword, name='sayHello'), 
    path('', index, name='index'),
    path('home/', index, name='home'),
]