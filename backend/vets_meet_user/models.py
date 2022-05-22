from django.db import models
from .models import Event
from .models import Venue
from .models import Branch

# Create your models here.


class VetsMeetUser():
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address =models.EmailField('User Email')
    address = models.CharField(max_length=125)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    branch =  models.CharField(max_length=10)
    time_served = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name