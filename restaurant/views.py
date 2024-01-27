"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu, Booking
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated




def index(request):
    return render(request, 'index.html', {})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def helloword(request):
    return HttpResponse("Hello World")    

# restaurant/views.py


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
   
class BookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
  



    



