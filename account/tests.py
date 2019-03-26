from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from django.shortcuts import reverse
User = get_user_model()
from .forms import CustomSignupForm
from .admin import UserCreationForm


# Create your tests here.
class RegistrationViewTestCase(TestCase):
    def setUp(self):
        # user = User.objects.create_user(username='hrtkkumar', email='hritikkumar.rd@gmail.com', password='password')
        pass
    
    def test_registration_view_get(self):
        """
        A ``GET`` to the ``register`` view uses the appropriate
        template and populates the registration form into the context.
        """

        response = self.client.get(reverse('account:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.failUnless(isinstance(response.context['form'], UserCreationForm)) 

    def test_registration_view_post_success(self):
        """
        A ``POST`` to the ``register`` view with valid data properly
        creates a new user and issues a redirect
        """
        response = self.client.post(reverse('account:signup'), 
                                        data={'username':'hrtkkumar',
                                            'email':'hritikkumar.rd@gmail.com',
                                            'password1':'password',
                                            'password2':'password'})
        self.assertEqual(response.status_code, 302)
        print(response.context)
        # self.failIf(response.context['form'].is_valid())
        self.assertRedirects(response, '/teams/')
        self.assertEqual(User.objects.count(), 1)
        self.client.login(username='hrtkkumar',password='password')
        response = self.client.get('/teams/',follwo=True)
        self.assertTrue(response.context['user'].is_authenticated)
    
    
        
