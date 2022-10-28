"""
Tests for the Django admin modifications
"""
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test for the admin site"""

    def setUp(self):
        """Setup for the test"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@exemple.com',
            password='testpass1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@exemple.com',
            password='testpass1234',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(res)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
