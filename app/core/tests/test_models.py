"""
Test for modesls
"""

from django.contrib.auth import get_user_model
from django.test import TestCase


class MyTestCase(TestCase):
    """Test creating a new user with no email raises error"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@exemplee.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_email = [
            ['test1@EXEMPLE.com', 'test1@exemple.com'],
            ['Test2@Exemple.com', 'Test2@exemple.com'],
            ['TEST3@EXEMPLE.COM', 'TEST3@exemple.com'],
            ['test4@exemple.COM', 'test4@exemple.com']
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'test123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@exemple.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
