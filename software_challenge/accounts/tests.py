from django.test import TestCase

# Create your tests here.
from django.test import (TestCase,
                         Client,
                         LiveServerTestCase,)

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import time, random, string
from django.contrib.auth import login

# create session cookie
from django.conf import settings
from django.contrib.auth import (
    SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY,
    get_user_model
)
from django.contrib.sessions.backends.db import SessionStore
User = get_user_model()

"""
Static method tools
for test cases
"""
class TestUtils:

    @staticmethod
    def make_user(test_obj, username, password):
        test_obj.username = username
        test_obj.password = password
        user = User.objects.create_user(username=username, password=password)
        user.set_password(password)
        user.save()

    @staticmethod
    def make_super_user(test_obj,\
                        username,\
                        password=User.objects.make_random_password(),\
                        email=''.join(random.choices(string.ascii_lowercase, k=12)) + "@gmail.com"):
        test_obj.su_username = username
        test_obj.su_password = password
        test_obj.su_email = email

        su = User.objects.create(username=username, password=password, email=email)
        su.set_password(password)
        su.is_staff = True
        su.is_superuser = True
        su.is_active = True
        su.save()

        test_obj.superuser = su


    @staticmethod
    def create_session_cookie(test_obj, username, password):
        # Create a new test user if not exist
        if not test_obj.username or not test_obj.password:
            TestUtils.make_user(test_obj, username, password)

        # Create the authenticated session using the new user credentials
        session = SessionStore()
        session[SESSION_KEY] = User.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session[HASH_SESSION_KEY] = User.get_session_auth_hash()
        session.save()

        # Finally, create the cookie dictionary
        cookie = {
            'name': settings.SESSION_COOKIE_NAME,
            'value': session.session_key,
            'secure': False,
            'path': '/',
        }
        return cookie

class UserTestCase(TestCase):

    def setUp(self):
        TestUtils.make_user(self,'testdev','testdevpassword')

    def test_user_exists(self):
        user = User.objects.get(username=self.username)
        self.assertIsNotNone(user)

    def test_user_string_representation(self):
        user = User.objects.get(username=self.username)
        self.assertEqual(str(user), self.username)

    def test_user_login_logout(self):
        # response = self.client.post('/accounts/login/', {'username': self.username, 'password': self.password},follow=True)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/accounts/password-change/', follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.logout()


class AdminTestCase(TestCase):

    def setUp(self):
        TestUtils.make_user(self,'testdev','testdevpassword')
        TestUtils.make_super_user(self,'testdev1')

    def test_admin_login_redirect(self):
        # try access superuser tools
        response = self.client.get('/admin/',follow=True)
        # check status code
        self.assertEqual(response.redirect_chain[0][1], 302)
        # check redirect to admin login
        self.assertRedirects(response, '/admin/login/?next=/admin/')

    def test_admin_login(self):
        response = self.client.post('/admin/login/', {'username': self.su_username, 'password': self.su_password},follow=True)
        self.assertEqual(response.status_code, 200)

    def test_admin_pages(self):
        # response = self.client.post('/admin/login/', {'username': self.su_username, 'password': self.su_password},follow=True)
        self.client.login(username=self.su_username, password=self.su_password)
        admin_pages = [
            "/admin/",
            "/admin/password_change/",
            # put all the admin pages for your models in here.
            "/admin/accounts/",
            "/admin/accounts/user/",
            "/admin/accounts/user/add/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            # "/admin/comments/",
            # "/admin/comments/comment/",
            # "/admin/comments/comment/add/",
            # "/admin/posts/",
            # "/admin/posts/post/",
            # "/admin/posts/post/add/",
        ]

        for page in admin_pages:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 200, msg="fetching "+page)
            self.assertTrue("<!DOCTYPE html" in str(resp.content))




class LiveTwitterTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(1)
        TestUtils.make_user(cls,'testdev','testdevpassword')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_live_login_logout(self):
        # create session cookie
        session_cookie = TestUtils.create_session_cookie(self, self.username, self.password)
        # add the newly created session cookie to selenium webdriver.
        self.selenium.add_cookie(session_cookie)
        # refresh to exchange cookies with the server.
        self.selenium.refresh()

        self.selenium.get('{}{}'.format(self.live_server_url, '/accounts/login/'))

        # find username input, enter username
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.username)

        # find password input, enter password
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.password)

        # click login
        self.selenium.find_element_by_xpath('//input[@value="Log In"]').click()

        # logout
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_xpath('//span[@value="Logout"]').click()
        time.sleep(3)

    def test_live_twitter_search(self):
        # login first
        self.client.login(username=self.username, password=self.password) #Native django test client
        cookie = self.client.cookies['sessionid']
        self.selenium.get(self.live_server_url + '/tweets/')  #selenium will set cookie domain based on current page domain
        self.selenium.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.selenium.refresh() #need to update page for logged in user
        self.selenium.get(self.live_server_url + '/tweets/')

        # request tweets search page
        self.selenium.get('{}{}'.format(self.live_server_url, '/tweets/'))

        # search twitter for tweets by PayTM
        search_input = self.selenium.find_element_by_name("usr_query")
        submit_input = self.selenium.find_element_by_name("submit_query")
        search_input.send_keys("@paytm")
        submit_input.click()
