from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class UserTestCase(TestCase):
    def test_user(self):
        username = 'dude'
        password = 'dude1234'
        user = User.objects.create(username = username)
        user.set_password(password)
        user.save
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))