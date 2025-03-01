from django.test import TestCase
from django.urls import reverse
from .models import ClientRecommendation


class RecommendationAPITest(TestCase):
    def setUp(self):
        ClientRecommendation.objects.create(client_id=1, product_name='Кредитная карта', recommendation_score=8)
        ClientRecommendation.objects.create(client_id=1, product_name='Сберегательный счет', recommendation_score=9)
        ClientRecommendation.objects.create(client_id=1, product_name='Ипотека', recommendation_score=7)

    def test_get_recommendations(self):
        response = self.client.get(reverse('recommendations', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 3)

