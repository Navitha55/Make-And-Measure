from django.db import models

# Create your models here.

class Dress(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    
class UserMeasurements(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    chest = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    shoulders = models.IntegerField()
    arm_length = models.IntegerField()
    fabric = models.CharField(max_length=50)
    dress_type = models.CharField(max_length=50)