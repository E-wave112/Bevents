from django.test import TestCase
# Create your tests here.

from .models import OrganizerProfile,EventUserProfile,UserBook,AuthUser

# class AuthTestUser(TestCase):
#     @classmethod
#     def setTestData(cls):
#         AuthUser.objects.create(
#             email="dwave101@gmail.com",username="Dwave"
#         )

#     def test_email(self):
#         auth = AuthUser.objects.get(pk=14)
#         expected_object_name = f'{auth.email}'
#         self.assertEquals(expected_object_name, 'dwave101@gmail.com')

#     def test_user(self):
#         auth = AuthUser.objects.get(pk=14)
#         expected_object_name = f'{auth.username}'
#         self.assertEquals(expected_object_name, 'Dwave')


##create a test case for the organizer profile model
class OrganizerTestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        OrganizerProfile.objects.create(
            name='Ewave', role='organizer',email_address="dwave101@gmail.com",location="Lagos State",
            phone_number="+2347045477824",supplementary_phone_number="+2347081927814",description="Good here",
            image="cloudinary.jpg",price=400.5,street_address="Yaba, Lagos"
        )

    def test_name(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.name}'
        self.assertEquals(expected_object_name, 'Ewave')

    def test_role(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.role}'
        self.assertEquals(expected_object_name, 'organizer')

    def test_email(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.email_address}'
        self.assertEquals(expected_object_name,'dwave101@gmail.com')

    def test_location(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.location}'
        self.assertEquals(expected_object_name,'Lagos State')

    def test_phone(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.phone_number}'
        self.assertEquals(expected_object_name,'+2347045477824')

    def test_supplement(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.supplementary_phone_number}'
        self.assertEquals(expected_object_name,'+2347081927814')

    def test_description(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.description}'
        self.assertEquals(expected_object_name,"Good here")

    def test_image(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.image}'
        self.assertEquals(expected_object_name,"cloudinary")
    
    def test_price(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.price}'
        self.assertEquals(expected_object_name,'400.50')

    
    def test_street(self):
        organizer = OrganizerProfile.objects.get(id=1)
        expected_object_name = f'{organizer.street_address}'
        self.assertEquals(expected_object_name,"Yaba, Lagos")

