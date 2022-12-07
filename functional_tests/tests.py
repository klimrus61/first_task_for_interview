from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from unittest import skip
from selenium.webdriver.common.keys import Keys

import time
import os

MAX_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):
    """Тест нового посетителя"""

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def wait_for(self, fn):
        '''Ожидать'''
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    

class RegistrationUserTest(FunctionalTest):
    '''тест регистрации пользователя'''
# •	Регистрация пользователей
    @skip
    def test_can_create_new_user(self):
        '''тест: можно добавить нового пользователя'''
        self.browser.get(self.live_server_url + '/admin')
        self.assertIn('Регистрация', self.browser.title)

        inputbox = self.browser.find_element_by_id('id_user_name')
        inputbox.send_keys('test')
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_new_user_password_1')



class AuthorizationUserTest(FunctionalTest):

    def test_can_authorization_admin(self):
        '''тест: admin может авторизоваться'''
# •	Аутентификация пользователей
        # Создается админский аккаунт
        admin = User.objects.create_superuser(username='admin', password='admin')
        
        # Данные вводятся в форму 
        self.browser.get(self.live_server_url + '/admin')
        inputbox_username = self.browser.find_element(By.NAME, 'username')
        inputbox_username.send_keys('admin')
        inputbox_password = self.browser.find_element(By.NAME, 'password')
        inputbox_password.send_keys('admin')
        self.browser.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()

        # Успешно открывается доступ в админскую часть
        self.assertIn('Site administration', self.browser.title)

    def test_can_authorization_user(self):
        '''тетс: пользователь может авторизоваться'''
        user = User.objects.create_user(username='test', password='testpassword')

        self.browser.get(self.live_server_url + '/accounts/login')
        inputbox_username = self.browser.find_element(By.NAME, 'username')
        inputbox_username.send_keys('test')
        inputbox_password = self.browser.find_element(By.NAME, 'password')
        inputbox_password.send_keys('testpassword')
        self.browser.find_element(By.NAME, 'login button').click()

        self.assertIs('Home page', self.browser.title)


        


# •	Зарегистрированные пользователи могут проходить любой из тестовых наборов
# •	Последовательный ответ на все вопросы, каждый вопрос должен выводится на новой странице с отправкой формы (перескакивать через тесты или оставлять неотмеченными нельзя)
# •	После завершения тестирования смотреть результат:
# •	количество правильных/неправильных ответов
# •	процент правильных ответов
