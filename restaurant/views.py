from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MenuItem
from .models import Menu, Booking, MenuItem
from .serializers import MenuItemSerializer, BookingSerializer, MenuSerializer
from django.utils import timezone
from django.shortcuts import render
from django.utils import timezone
from .models import MenuItem
from django.shortcuts import render
from django.utils import timezone
from .models import MenuItem
from .models import BookingModel
from .forms import BookingForm
from .models import BookingModel
from django.shortcuts import render
from django.shortcuts import render
from .models import BookingModel
import random
import string

# Create your views here. 
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemView(generics.ListCreateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    def get(self, request, pk):
        return Response(MenuItemSerializer(MenuItem.objects.get(pk=pk)).data)


class BookingView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

#def index(request):
#    return render(request, 'index1.html', {})

def index(request):
    menu_items = MenuItem.objects.all()
    current_year = timezone.now().year
    return render(request, 'index1.html', {'menu_items': menu_items, 'current_year': current_year})

def menu(request):
    menu_items = MenuItem.objects.all()
    current_year = timezone.now().year
    return render(request, 'menu.html', {'menu_items': menu_items, 'current_year': current_year})
    
def booking(request):
    booking = None  # Default value if the request method is not POST

    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        guests = request.POST.get('guests')
        time = request.POST.get('time')

        # Generate a confirmation number
        confirmation_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        # Save booking details to the database
        booking = BookingModel(name=name, email=email, guests=guests, time=time, confirmation_number=confirmation_number)
        booking.save()

    return render(request, 'booking.html', {'booking': booking})
    
def confirmation(request):
    return render(request, 'confirmation.html')
    
def about(request):
    return render(request, 'about.html', {'about': about})    
