from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)