from django.db import models
from phone_field import PhoneField
#pip install django-phone-field


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=122)
    address=models.TextField()
    message=models.TextField()
    
    
    def __str__(self) :
        return self.name
    