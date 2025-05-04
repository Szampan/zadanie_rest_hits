from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Hit, Artist


class HitViewSetTests(APITestCase):
    
    def setUp(self):
        self.artist = Artist.objects.create(first_name="Irving", last_name="Washington")
    
    def test_get_hits_list_empty(self):
        # arrange
        url = reverse('hit-list')
        # act
        response = self.client.get(url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    @patch('rest_framework.pagination.PageNumberPagination.page_size', 3)
    def test_get_hits_list(self):
        # arrange
        hits_count = 5
        for i in range(hits_count):
            Hit.objects.create(title=f"test hit {i}", artist=self.artist)
        url = reverse('hit-list')
        # act
        response = self.client.get(url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], hits_count)
        self.assertEqual(len(response.data['results']), 3)

    def test_get_hit_detail(self):
        # arrange
        hit = Hit.objects.create(title="test hit", artist=self.artist)
        url = reverse('hit-detail', kwargs={'title_url': hit.title_url})
        expected_data = {
            'id': hit.id,
            'title': hit.title,
            'artist': hit.artist.id,
            'title_url': hit.title_url,
            'created_at': hit.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': hit.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        # act
        response = self.client.get(url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_get_hit_detail_not_found(self):
        # arrange
        url = reverse('hit-detail', kwargs={'title_url': 'non-existing-title'})
        # act
        response = self.client.get(url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_hit(self):
        # arrange
        url = reverse('hit-list')
        hit_title = 'test title'
        data = {
            'title': hit_title,
            'artist': self.artist.id
        }
        # act
        response = self.client.post(url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hit.objects.count(), 1)
        self.assertEqual(Hit.objects.get().title, hit_title)

    def test_create_hit_invalid_data(self):
        # arrange
        url = reverse('hit-list')
        data = {
            'title': '',
            'artist': self.artist.id
        }
        # act
        response = self.client.post(url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_hit(self):
        # arrange
        hit = Hit.objects.create(title="test hit", artist=self.artist)
        new_artist = Artist.objects.create(first_name="John", last_name="Doe")        
        new_title = "updated title"
        data = {
            'title': new_title,
            'artist': new_artist.id
        }
        url = reverse('hit-detail', kwargs={'title_url': hit.title_url})
        # act
        response = self.client.put(url, data, format='json')
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hit.objects.get().title, new_title)
        self.assertEqual(Hit.objects.get().artist, new_artist)
    
    def test_delete_hit(self):
        # arrange
        hit = Hit.objects.create(title="test title", artist=self.artist)
        url = reverse('hit-detail', kwargs={'title_url': hit.title_url})
        # act
        response = self.client.delete(url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Hit.objects.all())

    def test_delete_hit_not_found(self):
        # arrange
        url = reverse('hit-detail', kwargs={'title_url': 'non existing title'})
        # act
        response = self.client.delete(url)
        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class PopulateDbCommandTest(TestCase):
    def test_populate_db_command(self):
        # act
        call_command('populate_db')
        # assert
        self.assertEqual(Artist.objects.count(), 3)
        self.assertEqual(Hit.objects.count(), 20)
        self.assertFalse(Hit.objects.filter(artist=None))