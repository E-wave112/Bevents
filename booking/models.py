from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import requests
from django.core.validators import RegexValidator

from .managers import CustomUserManager



###write a regex to validate phone numbers in django
phone_regex = RegexValidator(
        regex=r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$',
        message='this field must be a  valid phone number 📱 !'
        
    )


##create a custom user who visit the event site authentication model
class AuthUser(AbstractUser):
    STATUS_API_CHOICES = []
    ##fetch states api
    states = requests.get('https://countryrestapi.herokuapp.com/ng/').json()
    for i in states['states']:
        STATUS_API_CHOICES.append((f"{i}",i))
        ##convert the choices list to a tuple
        x = tuple(STATUS_API_CHOICES)

    STATUS_CHOICES = (
    ('user', 'User'),
    ('organizer', 'Organizer'),
    )
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=100,choices=x,default="Lagos State")
    role =  models.CharField(max_length=100,choices=STATUS_CHOICES,default='user')

    ##set the email field as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','location','role']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class OrganizerProfile(models.Model):
    name = models.CharField(max_length=100,unique=True)
    role =  models.OneToOneField(AuthUser,on_delete=models.CASCADE, primary_key=True,related_name='auth_user')
    email_adress = models.ForeignKey(AuthUser,on_delete=models.CASCADE,related_name='auth_email')
    location = models.OneToOneField(AuthUser,on_delete=models.CASCADE,related_name='auth_location')
    phone_number= models.CharField(validators=[phone_regex],max_length=100)
    description = models.TextField()
    event_photo = models.ImageField(upload_to='photos/',blank=True)
    price = models.DecimalField(max_digits=100,decimal_places=3)
    street_address = models.CharField(max_length=200)


class EventUserProfile(models.Model):
    name = models.CharField(max_length=100,unique=True)
    role =  models.OneToOneField(AuthUser,on_delete=models.CASCADE, primary_key=True,related_name='auth_user_event')
    email_adress = models.ForeignKey(AuthUser,on_delete=models.CASCADE,related_name='auth_email_event')
    location = models.OneToOneField(AuthUser,on_delete=models.CASCADE,related_name='auth_location_event')
    phone_number= models.CharField(validators=[phone_regex],max_length=100)
    profile_photo = models.ImageField(upload_to='user/',blank=True)



