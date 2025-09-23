from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Nacionalidad

class NacionalidadAPITests(APITestCase):
    def setUp(self):
        self.nacionalidad = Nacionalidad.objects.create(pais="Test Country", nacionalidad="Test Nationality")

    def test_get_nacionalidades(self):
        """
        Ensure we can get the list of nacionalidades.
        """
        url = reverse('nacionalidad-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_nacionalidad(self):
        """
        Ensure we can create a new nacionalidad.
        """
        url = reverse('nacionalidad-list')
        data = {'pais': 'New Country', 'nacionalidad': 'New Nationality'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Nacionalidad.objects.count(), 2)
        self.assertEqual(Nacionalidad.objects.get(id=response.data['id']).pais, 'New Country')

    def test_get_nacionalidad(self):
        """
        Ensure we can get a single nacionalidad.
        """
        url = reverse('nacionalidad-detail', kwargs={'pk': self.nacionalidad.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pais'], 'Test Country')

    def test_update_nacionalidad(self):
        """
        Ensure we can update a nacionalidad.
        """
        url = reverse('nacionalidad-detail', kwargs={'pk': self.nacionalidad.pk})
        data = {'pais': 'Updated Country', 'nacionalidad': 'Updated Nationality'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.nacionalidad.refresh_from_db()
        self.assertEqual(self.nacionalidad.pais, 'Updated Country')

    def test_delete_nacionalidad(self):
        """
        Ensure we can delete a nacionalidad.
        """
        url = reverse('nacionalidad-detail', kwargs={'pk': self.nacionalidad.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Nacionalidad.objects.count(), 0)
