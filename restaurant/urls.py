from django.contrib import admin 
from django.urls import path 
from .views import helloword, index, MenuItemView, SingleMenuItemView, BookViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'booking', BookViewSet, basename='booking')


urlpatterns = [ 
    path('sayhello', helloword, name='sayHello'), 
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    
    path('booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
   
]