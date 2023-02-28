from pyexpat import model
from django.db import models

from manage import main

# Create your models here.
class Learners(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Parents(models.Model):
    parent= models.ForeignKey(Learners, on_delete=models.CASCADE)
    pname = models.CharField(max_length=200)
    complited = models.BooleanField()
    def __str__(self):
        return self.pname

#python3 manage.py makemigrations bot
#python3 manage.py migrition