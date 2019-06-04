from django.db import models
from .validators import (validate_password_length, validate_password_digit, 
                         validate_password_uppercase,validate_username_length, validate_username_alphadigits)
# Create your models here.

class Siteuser(models.Model):
    username= models.CharField(max_length=25, verbose_name= 'User name', validators= [validate_username_length, validate_username_alphadigits])
    password1= models.CharField(max_length=30, validators=[validate_password_length, validate_password_digit, validate_password_uppercase])
    password2= models.CharField(max_length=30)
    
    def __str__(self):
        return self.username