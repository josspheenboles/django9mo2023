from django.db import models

# Create your models here.
class Catagory(models.Model):
    id=models.AutoField(primary_key=True,db_column='ID' )
    name=models.CharField(max_length=30,db_column='Name')
    def __str__(self):
        return  self.name

class Task(models.Model):
    id=models.AutoField(primary_key=True,db_column='ID')
    name=models.CharField(max_length=100,db_column='Name')
    catagoryobj=models.ForeignKey(Catagory,to_field='id',on_delete=models.CASCADE,db_column='Catagory_ID')