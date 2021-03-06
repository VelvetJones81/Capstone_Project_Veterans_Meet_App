from tkinter import CASCADE
from django.db import models
from branch.models import Branch

# Create your models here.
class VeteranUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address =models.EmailField('User Email')
    address = models.CharField(max_length=125)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    branch =  models.ForeignKey(Branch, max_length=20, on_delete= models.CASCADE)
    time_served = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name +' ' + self.last_name
