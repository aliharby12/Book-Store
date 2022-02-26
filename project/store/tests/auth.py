from django.test import TestCase

from django.urls import reverse

from project.store.models import User

from model_bakery import baker


class UserRegisterTests(TestCase):
    """basic test cases for user register"""

    def setUp(self) -> None:
        self.email = 'testuser@email.com'
        self.first_name = 'test'
        self.last_name = 'user'
        self.password = 'test@1234'

    def test_register_page_url(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_register_form(self):
        response = self.client.post(reverse('register'), data={
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

        users = User.objects.all()
        self.assertEqual(users.count(), 1)


class UserLoginTests(TestCase):
    """basic test cases for user login"""

    def setUp(self):
        self.user = baker.make(User)

    def test_login_page_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_login(self):
        response = self.client.post(
            reverse('login'), {'email':self.user.email, 'password':self.user.password}, follow=True
        )
        self.assertEqual(response.status_code, 200)