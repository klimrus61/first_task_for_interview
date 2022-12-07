from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    '''Тест модели пользователя'''


class AccountsViewTest(TestCase):
    """Тест представления аккаунтов"""

    def test_uses_login_template(self):
        """тест: используется шаблон login"""
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_validate_data_from_form_login(self):
        """тест: валидация данных из отправленной формы"""
        user = User.objects.create_user(username='test', password='test')

        response = self.client.post('/accounts/login/', {'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

        response = response = self.client.post('/accounts/login/', {'username': 'wrong_user', 'password': 'wrong_password'})
        self.assertNotEqual(response.status_code, 200)
        print(response.status_code)