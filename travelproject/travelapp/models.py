from django.db import models


# Create your models here.

class place(models.Model):  # here place is the table
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')  # pics is the folder where we going to store images
    desc = models.TextField()


class team(models.Model):
    tname = models.CharField(max_length=150)
    timg = models.ImageField(upload_to='pics')
    desig = models.CharField(max_length=200)
    tabot = models.TextField()