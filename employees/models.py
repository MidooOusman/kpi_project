from django.db import models
from datetime import datetime
from managers.models import Manager

class Employee(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    titel = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    price = models.TextField(blank=True)
    bedrooms  = models.IntegerField()
    bathrooms= models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    phto_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phto_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phto_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phto_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phto_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phto_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phto_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date  = models.DateTimeField(default= datetime.now, blank= True)
    def __str__(self):
        return self.titel 

