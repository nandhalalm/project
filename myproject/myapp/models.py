from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    place = models.CharField( max_length=100,null=True,blank=True)
    designation =models.CharField(max_length=100)
   # email = models.EmailField(unique=True)
    img = models.FileField(null=True, blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.name

