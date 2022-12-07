from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class AccountsViewTest(TestCase):
    """Тест представления аккаунтов"""

    def test_uses_login_template(self):
        """тест: используется шаблон login"""
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'login.html')

