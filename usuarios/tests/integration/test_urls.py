from django.urls import reverse, resolve

class TestUrls:

    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_logout_url(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def test_signin_url(self):
        path = reverse('signin')
        assert resolve(path).view_name == 'signin'

    def test_update_url(self):
        path = reverse('update')
        assert resolve(path).view_name == 'update'