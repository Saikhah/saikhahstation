import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  
    price = models.IntegerField()            
    description = models.TextField()         
    thumbnail = models.URLField()            
    category = models.CharField(max_length=100)  
    is_featured = models.BooleanField(default=False)  

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     persona = models.TextField()

    def __str__(self):
        return self.name

