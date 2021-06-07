from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


# Create your tests here.
class FunctionalUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_users_should_return_200(self):
        response = self.client.get(reverse("get_all"))
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.client.get(reverse("get_one", kwargs={"uid": 10}), format="json")
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(reverse("create"))
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.client.put(reverse("update", kwargs={"uid": 10}), format="json")
        self.assertEqual(response.status_code, 200)
    
    def test_delete_user(self):
        response = self.client.delete(reverse("delete", kwargs={"uid": 10}), format="json")
        self.assertEqual(response.status_code, 200)
