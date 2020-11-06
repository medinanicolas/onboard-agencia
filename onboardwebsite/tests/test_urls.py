from django.test import SimpleTestCase
from django.urls import reverse,resolve
from onboardwebsite.views import index,galeria,contacto,registro

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('onboardwebsite:index')
        self.assertEquals(resolve(url).func,index)

    def test_galeria_url_is_resolved(self):
        url = reverse('onboardwebsite:galeria')
        self.assertEquals(resolve(url).func,galeria)

    def test_contacto_url_is_resolved(self):
        url = reverse('onboardwebsite:contacto')
        self.assertEquals(resolve(url).func,contacto)

    def test_registro_url_is_resolved(self):
        url = reverse('onboardwebsite:registro')
        self.assertEquals(resolve(url).func,registro)
        