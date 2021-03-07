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

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=100,unique=True)
   

    ##set the email field as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email



##choices for ths states using third party apis
STATUS_API_CHOICES = []
##fetch states api
states = requests.get('https://countryrestapi.herokuapp.com/ng/').json()
for i in states['states']:
    STATUS_API_CHOICES.append((f"{i}",i))
    ##convert the choices list to a tuple
x = tuple(STATUS_API_CHOICES)

##user choices api
STATUS_CHOICES = (('user', 'User'),
('organizer', 'Organizer'),)




class OrganizerProfile(models.Model):

    name = models.CharField(max_length=100,unique=True)
    role = models.CharField(max_length=100,choices=STATUS_CHOICES,default='organizer')
    email_adress = models.ForeignKey(AuthUser,on_delete=models.CASCADE,related_name='auth_email')
    location = models.CharField(max_length=100,choices=x,default="Lagos State")
    phone_number= models.CharField(validators=[phone_regex],max_length=100)
    description = models.TextField()
    event_photo = models.ImageField(upload_to='organizer/',blank=True)
    price = models.DecimalField(max_digits=100,decimal_places=3)
    street_address = models.CharField(max_length=200)


    ##define a string method
    def __str__(self):

        return self.location, self.role



class EventUserProfile(models.Model):
    name = models.CharField(max_length=100,unique=True)
    role = models.CharField(max_length=100,choices=STATUS_CHOICES,default='user')
    email_adress = models.ForeignKey(AuthUser,on_delete=models.CASCADE,related_name='auth_email_event')
    location = models.CharField(max_length=100,choices=x,default="Lagos State")
    phone_number= models.CharField(validators=[phone_regex],max_length=100)
    profile_photo = models.ImageField(upload_to='user/',blank=True)

    ##define a string method
    def __str__(self):
        
        return self.location, self.role



