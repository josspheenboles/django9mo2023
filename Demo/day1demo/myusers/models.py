from django.db import models

# Create your models here.
class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    username=models.CharField(max_length=20)
    Password=models.CharField(max_length=12)