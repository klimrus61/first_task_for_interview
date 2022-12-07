from django.test import TestCase


class AccountsViewTest(TestCase):
    """Тест представления аккаунтов"""

    def test_uses_login_template(self):
        """тест: используется шаблон login"""
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'login.html')
