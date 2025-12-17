"""Tests for API application."""
from http import HTTPStatus

from django.test import Client, TestCase
from api import models


class TaskiAPITestCase(TestCase):
    """Test case for Taski API."""

    def setUp(self):
        """Set up test client."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Check if task list is accessible."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Check if task can be created."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
