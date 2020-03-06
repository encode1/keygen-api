from django.test import TestCase
from django.utils import timezone
from .models import Key, Account


# models test
class AccountTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            email='test@example.com')
        self.account.save()

    def tearDown(self):
        self.account.delete()

    def test_account_creation(self):
        self.assertTrue(isinstance(self.account, Account))
        self.assertEqual(self.account.__str__(), self.account.email)


class KeyTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            email='test@example.com')
        self.account.save()
        self.key = Key.objects.create(
            hash_key='hash_key', account=self.account)

    def tearDown(self):
        self.key.delete()

    def test_key_creation(self):
        self.assertTrue(isinstance(self.key, Key))
        self.assertEqual(self.key.__str__(), self.key.hash_key)
