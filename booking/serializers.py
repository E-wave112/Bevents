from rest_framework import serializers
from .models import EventUserProfile,OrganizerProfile,AuthUser,UserBook


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUserProfile
        fields = ( 'id','name','role','email_address','location','image','phone_number')

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizerProfile
        fields = ( 'id', 'name','role','email_address','location', 'phone_number','description','image','price','street_address')


class RegisteredUsers(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('email','username','password')


class BookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ('email_address','allotted_budget','date_of_event','event_type','estimated_no_of_guests')
        
