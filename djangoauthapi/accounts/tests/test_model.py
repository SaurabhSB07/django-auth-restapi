from accounts.models import User  
from django.test import TestCase

class AccModelsTest(TestCase):
    def test_create_user(self):
        email = "test@example.com"
        name = "Test User"
        password = "strongpassword123"

        user = User.objects.create_user(email=email, name=name, password=password)  
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)




        
