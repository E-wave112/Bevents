from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import requests
from decouple import config
from django.core.validators import RegexValidator
from .managers import CustomUserManager
# cloudinary items for uploading media files to the cloud
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField


cloudinary.config(
    cloud_name = config('CLOUD_NAME'),
   api_key = config('CLOUDINARY_KEY'),
   api_secret = config('CLOUDINARY_SECRET')
)



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
STATUS_CHOICES = (
    ('user', 'User'),
('organizer', 'Organizer'),
)

EVENT_CHOICES= (
    ('wedding','Wedding'),
    ('birthday','Birthday'),
    ('others','Others'),
    ('conferences','Conferences'),
    ('competitions','Competitions'),
    ('expo','Expo'),
)

AVAILABILITY_CHOICES = (
    ('yes','YES'),
    ('no','NO'),
)




class OrganizerProfile(models.Model):
    name = models.CharField(max_length=100,unique=True)
    role = models.CharField(max_length=100,choices=STATUS_CHOICES,default='organizer')
    email_address = models.ForeignKey(AuthUser,on_delete=models.CASCADE,related_name='auth_email')
    # email_address = models.CharField(max_length=50)
    location = models.CharField(max_length=100,choices=x,default="Lagos State")
    phone_number= models.CharField(validators=[phone_regex],max_length=100,unique=True)
    supplementary_phone_number= models.CharField(validators=[phone_regex],max_length=100,unique=True,null=True)
    description = models.TextField()
    image = CloudinaryField('image',blank=True)
    price = models.DecimalField(max_digits=100,decimal_places=2)
    street_address = models.CharField(max_length=200)



    ##define a string method
    def __str__(self):
        return self.name



class EventUserProfile(models.Model):
    email_address = models.ForeignKey(AuthUser,on_delete=models.CASCADE,related_name='auth_email_event')
    name = models.CharField(max_length=100,unique=False)
    # email_address = models.CharField(max_length=50)
    role = models.CharField(max_length=100,choices=STATUS_CHOICES,default='user')
    location = models.CharField(max_length=100,choices=x,default="Lagos State")
    phone_number= models.CharField(validators=[phone_regex],max_length=100,unique=True)
    image = CloudinaryField('image',blank=True)

    ##define a string method
    def __str__(self):
        return self.name

#create a model for when a user books an event
class UserBook(models.Model):
    email_address=models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    allotted_budget=models.DecimalField(max_digits=30, decimal_places=3)
    date_of_event=models.DateField(auto_now=False, auto_now_add=False)
    event_type=models.CharField(max_length=100,choices=EVENT_CHOICES,default='choose your event type here !')
    estimated_no_of_guests=models.IntegerField()
    available = models.CharField(max_length=100,choices=AVAILABILITY_CHOICES,default='no')
    def __str__(self):
        return self.event_type

        # http://127.0.0.1:8000/api/v1/book-edit/5


