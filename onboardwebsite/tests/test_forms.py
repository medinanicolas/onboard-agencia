from django.test import SimpleTestCase
from onboardwebsite.forms import ExperienciasUsuario


class Testforms(SimpleTestCase):

    def test_post_form_valido(self):
        form = ExperienciasUsuario(
            data=
            {
            "titulo": "hola",
            "calificacion" : 0,
            "mensaje": "caro",
            })
        self.assertTrue(form.is_valid())
    
    def test_post_form_vacio(self):
        form = ExperienciasUsuario(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)