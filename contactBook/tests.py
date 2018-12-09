from django.test import TestCase
from contactBook.models import Contact
from .ApiV1_0 import ApiContact

# models test
class ContactModelTestCase(TestCase):
    """
    This class defines the test suite for the contact model.
    """

    def setUp(self):
        self.contact_name = 'test'
        self.contact_email = 'test@test.com'

        self.contact = Contact(Name=self.contact_name, EmailId=self.contact_email)

    def test_model_can_create_a_contact(self):

        """Test the contact model can create a contact."""

        old_count = Contact.objects.count()
        self.contact.save()
        new_count = Contact.objects.count()
        self.assertNotEqual(old_count, new_count)

    def testCreateContact(self):

        """Test the contact Api function can create a contact."""

        request = {'Name': 'Test', 'EmailId': 'test@test.com', 'PhoneNumber': '4373270'}
        returnData = ApiContact.addContact(self, request, format=None)
        self.assertEquals(returnData,"Success")

class SearchTestCase(TestCase):
    """Test suite for the search api ."""
    def testSearchContact(self):
        request = {'Name': 'Test', 'EmailId': 'test1@test.com', 'PhoneNumber': '4373270'}
        returnData = ApiContact.addContact(self, request, format=None)
        request = {'Name': 'Test','page':1}
        returnData = ApiContact.searchContact(self, request, format=None)
        self.assertEquals(returnData[0]['Name'], "Test")
        request = {'EmailId': 'test1@test.com', 'page': 1}
        returnData = ApiContact.searchContact(self, request, format=None)
        self.assertEquals(returnData[0]['EmailId'], "test1@test.com")

    def testSearchContactByName(self):
        request = {'Name': 'Test', 'EmailId': 'test1@test.com', 'PhoneNumber': '4373270'}
        returnData = ApiContact.addContact(self, request, format=None)
        request = {'Name': 'Test', 'page': 1}
        returnData = ApiContact.searchContactByName(self, request, format=None)
        self.assertEquals(returnData[0]['Name'], "Test")

    def testSearchContactByEmail(self):
        request = {'Name': 'Test', 'EmailId': 'test1@test.com', 'PhoneNumber': '4373270'}
        returnData = ApiContact.addContact(self, request, format=None)
        request = {'EmailId': 'test1@test.com', 'page': 1}
        returnData = ApiContact.searchContactByEmail(self, request, format=None)
        self.assertEquals(returnData[0]['EmailId'], "test1@test.com")



