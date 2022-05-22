from audioop import maxpp
from django.db import models

# Create your models here.

class Branch():
    branch = models.CharField(max_length=10)
    rank = models.CharField(max_length=50)
