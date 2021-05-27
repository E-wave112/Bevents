from django.test import TestCase
# Create your tests here.

from .models import OrganizerProfile,EventUserProfile,UserBook,AuthUser

class AuthTestUser(TestCase):
    @classmethod
    def setTestData(cls):
        auth_user = AuthUser.objects.create_user(
            email="dwaveflux@gmail.com",password="hullabaloooo"
        )
        
        auth_user.save()


    def test_email(self):
        try:
            auth = AuthUser.objects.get(id=1)
            expected_object_name = f'{auth.email}'
            expected_object_pass = f'{auth.password}'
            self.assertEqual(expected_object_name, 'dwaveflux@gmail.com')
            self.assertEqual(expected_object_pass, 'hullabaloooo')

        except AuthUser.DoesNotExist:
            auth = None


    # def test_user(self):
    #     auth = AuthUser.objects.get(id=1)
    #     expected_object_name = f'{auth.password}'
    #     self.assertEquals(expected_object_name, 'hullabaloooo')


# ##create a test case for the organizer profile model
class OrganizerTestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        auth_user = AuthUser.objects.create_user(
            email="dwaveflux@gmail.com",password="hullabaloooo"
        )

        auth_user.save()
        
        organizers_prof = OrganizerProfile.objects.create(
            name='Ewave', role='organizer',email_address=auth_user,location="Lagos State",
            phone_number="+2347045477824",supplementary_phone_number="+2347081927814",description="Good here",
            image="cloudinary.jpg",price=400.5,street_address="Yaba, Lagos"
        )

        organizers_prof.save()



    def test_organizer_instance(self):
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
        self.assertEquals(expected_object_name,'dwaveflux@gmail.com')

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


##write further test cases for the userprofile model

class UserTestBook(TestCase):

    @classmethod
    def setTestData(cls):
        EventUserProfile.objects.create(
            name="Ewave",role="user", email_address="dwaveflux@gmail.com",
            location="Lagos State", phone_number="+2347045477824",
            image="http://res.cloudinary.com/e-wave/image/upload/v1615919129/rbloqmw2hwxn4nfetcco.png"
        )


    def test_name(self):
        user = EventUserProfile.objects.get(id=1)
        expected_object_name = f'{user.name}'
        self.assertEquals(expected_object_name, 'Ewave')

    def test_role(self):
        user = EventUserProfile.objects.get(id=1)
        expected_object_name = f'{user.role}'
        self.assertEquals(expected_object_name, 'user')

    def test_email(self):
        user = EventUserProfile.objects.get(id=1)
        expected_object_name = f'{user.email_address}'
        self.assertEquals(expected_object_name,'dwaveflux@gmail.com')

    def test_location(self):
        user = EventUserProfile.objects.get(id=1)
        expected_object_name = f'{user.location}'
        self.assertEquals(expected_object_name,'Lagos State')

    def test_phone(self):
        user = EventUserProfile.objects.get(id=1)
        expected_object_name = f'{user.phone_number}'
        self.assertEquals(expected_object_name,'+2347045477824')

    def test_image(self):
        user = EventUserProfile.objects.get(id=1)
        expected_object_name = f'{user.image}'
        self.assertEquals(expected_object_name,"http://res.cloudinary.com/e-wave/image/upload/v1615919129/rbloqmw2hwxn4nfetcco.png")

