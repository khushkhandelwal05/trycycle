from django.db import models

# Create your models here.

class userinfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    room_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    

class Bookings(models.Model):
    user=models.CharField(max_length=40)
    slot=models.TextField()   

class contact_us(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=75)
    subject=models.TextField()
    feed=models.TextField()