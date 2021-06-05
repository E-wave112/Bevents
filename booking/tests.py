from django.test import TestCase
# Create your tests here.

from .models import OrganizerProfile,EventUserProfile,UserBook,AuthUser
# 1
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

# 2

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


    try:

        def test_organizer_instance(self):
            organizer = OrganizerProfile.objects.get(id=1)
            name = f'{organizer.name}'
            role = f'{organizer.role}'
            email = f'{organizer.email_address}'
            location = f'{organizer.location}'
            phone_number = f'{organizer.phone_number}'
            supplementary = f'{organizer.supplementary_phone_number}'
            description = f'{organizer.description}'
            image = f'{organizer.image}'
            price = f'{organizer.price}'
            street = f'{organizer.street_address}'
            self.assertEquals(name, 'Ewave')
            self.assertEquals(role, 'organizer')
            self.assertEquals(email,'dwaveflux@gmail.com')
            self.assertEquals(location,'Lagos State')
            self.assertEquals(phone_number,'+2347045477824')
            self.assertEquals(supplementary,'+2347081927814')
            self.assertEquals(description,"Good here")
            self.assertEquals(image,"cloudinary")
            self.assertEquals(price,'400.50')
            self.assertEquals(street,"Yaba, Lagos")

    except OrganizerProfile.DoesNotExist:
        organizer = None


        # def test_role(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.role}'
        #     self.assertEquals(expected_object_name, 'organizer')

        # def test_email(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.email_address}'
        #     self.assertEquals(expected_object_name,'dwaveflux@gmail.com')

        # def test_location(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.location}'
        #     self.assertEquals(expected_object_name,'Lagos State')

        # def test_phone(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.phone_number}'
        #     self.assertEquals(expected_object_name,'+2347045477824')

        # def test_supplement(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.supplementary_phone_number}'
        #     self.assertEquals(expected_object_name,'+2347081927814')

        # def test_description(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.description}'
        #     self.assertEquals(expected_object_name,"Good here")

        # def test_image(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.image}'
        #     self.assertEquals(expected_object_name,"cloudinary")
        
        # def test_price(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.price}'
        #     self.assertEquals(expected_object_name,'400.50')

        
        # def test_street(self):
        #     organizer = OrganizerProfile.objects.get(id=1)
        #     expected_object_name = f'{organizer.street_address}'
        #     self.assertEquals(expected_object_name,"Yaba, Lagos")


#write further test cases for the userprofile model

# 3

class UserTestEvent(TestCase):

    @classmethod
    def setTestData(cls):
        auth_user = AuthUser.objects.create_user(
            email="dwaveflux@gmail.com",password="hullabaloooo"
        )
        auth_user.save()


        event_user = EventUserProfile.objects.create(
            name="Ewave",role="user", email_address="dwaveflux@gmail.com",
            location="Lagos State", phone_number="+2347045477824",
            image="http://res.cloudinary.com/e-wave/image/upload/v1615919129/rbloqmw2hwxn4nfetcco.png"
        )

        event_user.save()

    try:


        def test_user(self):
            user = EventUserProfile.objects.get(name="Ewave")
            username = f'{user.name}'
            role = f'{user.role}'
            user_email=f'{user.email_address}'
            location = f'{user.location}'
            phone_number = f'{user.phone_number}'
            image = f'{user.image}'
            self.assertEquals(username, 'Ewave')
            self.assertEquals(role, 'user')
            self.assertEquals(user_email,'dwaveflux@gmail.com')
            self.assertEquals(location,'Lagos State')
            self.assertEquals(phone_number,'+2347045477824')
            self.assertEquals(image,"http://res.cloudinary.com/e-wave/image/upload/v1615919129/rbloqmw2hwxn4nfetcco.png")

    except EventUserProfile.DoesNotExist:
        user = None

        # def test_role(self):
        #     user = EventUserProfile.objects.get(id=1)
        #     expected_object_name = f'{user.role}'
        #     self.assertEquals(expected_object_name, 'user')

        # def test_email(self):
        #     user = EventUserProfile.objects.get(id=1)
        #     expected_object_name = f'{user.email_address}'
        #     self.assertEquals(expected_object_name,'dwaveflux@gmail.com')

        # def test_location(self):
        #     user = EventUserProfile.objects.get(id=1)
        #     expected_object_name = f'{user.location}'
        #     self.assertEquals(expected_object_name,'Lagos State')

        # def test_phone(self):
        #     user = EventUserProfile.objects.get(id=1)
        #     expected_object_name = f'{user.phone_number}'
        #     self.assertEquals(expected_object_name,'+2347045477824')

        # def test_image(self):
        #     user = EventUserProfile.objects.get(id=1)
        #     expected_object_name = f'{user.image}'
        #     self.assertEquals(expected_object_name,"http://res.cloudinary.com/e-wave/image/upload/v1615919129/rbloqmw2hwxn4nfetcco.png")



##write a unit test for the userbook model
class UserBookTest(TestCase):
    def UserBookTest(cls):
        user_book = UserBook.objects.create(
            email_address='dwave100@yahoo.com',
            allotted_budget=1340.50,
    date_of_event='2020-08-21',
    event_type='expo',
    estimated_no_of_guests=30,
    available='no'
        )
        user_book.save()
    try:
        def test_user_book(self):
            userbook = UserBook.objects.get(id=1)
            email=f'{userbook.email_address}'
            budget=f'{userbook.allotted_budget}'
            ddate=f'{userbook.date_of_event}'
            event=f'{userbook.event_type}'
            guests=f'{userbook.estimated_no_of_guests}'
            available=f'{userbook.available}'
            self.assertEquals(email,'dwave100@yahoo.com')
            self.assertEquals(budget,1340.50)
            self.assertEquals(ddate,'2020-08-21')
            self.assertEquals(event,'expo')
            self.assertEquals(guests,30)
            self.assertEquals(available,'no')
    
    except UserBook.DoesNotExist:
        userbook = None

        
