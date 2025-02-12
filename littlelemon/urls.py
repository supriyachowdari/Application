"""littlelemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

# # Path hack.
# import sys, os
# sys.path.insert(0, os.path.abspath('..'))
from restaurant import views


router = DefaultRouter()
router.register(r'tables', views.BookingView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('', views.index, name='home'),
    path('auth/', include('djoser.urls.authtoken')),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('about/', views.about, name='about'),
    path('order-online/', views.order_online, name='order_online'),
    path('order/', views.order_form, name='order_form'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('payment/<int:order_id>/', views.payment_page, name='payment_page'),
    path('process_payment/<int:order_id>/', views.process_payment, name='process_payment'),
    path('order-success/', views.order_success, name='order_success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
