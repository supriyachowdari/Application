from django.db import models


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