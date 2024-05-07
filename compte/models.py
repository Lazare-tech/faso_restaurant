from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser):
    phone_number=PhoneNumberField(max_length=20,verbose_name='Numero de telephone')
    is_restaurant= models.BooleanField(default=False,verbose_name='Est restaurant')