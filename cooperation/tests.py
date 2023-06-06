from django.test import TestCase, Client
from django.urls import reverse


class CooperationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {
            'company': 'test_company',
            'name': 'test_name',
            'phone': '12345678',
            'email': 'test@test.to',
            'text': 'test_text_123567',
        }

    def test_cooperation_view(self):
        response = self.client.get(reverse('cooperation:distribution'))

        self.assertEqual(response.status_code, 200)

    def test_cooperation_create(self):
        response = self.client.post(reverse('cooperation:distribution'), data=self.data)

        self.assertEqual(response.status_code, 302)
