from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@something.com', password='test123'):
    """create a sample user"""
    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):

    def test_creat_user_with_email_successful(self):
        """ create user w/ email"""
        email = 'test@something.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email for a new user is normalized"""
        email = 'test@SOMETHING.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """test creating user with email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    
    def test_create_new_superuser(self):
        """test creating a new user"""
        user = get_user_model().objects.create_superuser(
            'test@something.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
    
    def test_ingredient_str(self):
        """test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        
        self.assertEqual(str(ingredient), ingredient.name)