from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.title}: {str(self.price)}:'


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
        
class BookingModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    guests = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name 
        
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    guests = models.IntegerField()
    time = models.DateTimeField()
    confirmation_number = models.CharField(max_length=10)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    order_details = models.TextField()

    def __str__(self):
        return self.customer_name  # Or any other meaningful representation

class Payment(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.order_id} - {self.user.username} - {self.amount}"