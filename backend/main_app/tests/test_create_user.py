from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Catalog, AppUser as User
from ..serializers import CreateUserSerializer, UserSerializer


class TestCreateAndGetSingleUser(APITestCase):
    test_user = {
        "email": "test@gmail.com",
        "username": "test@gmail.com",
        "password": "test123",
    }

    def setUp(self):
        serializer = CreateUserSerializer(data=self.test_user)
        if serializer.is_valid():
            serializer.save()
            self.valid_user = serializer.data
            # print(serializer.data)
            # print(self.valid_user)
        else:
            print("invalid user")

    def test_get_valid_user(self):
        response = self.client.get(
            reverse("user_detail", kwargs={"pk": self.valid_user["id"]})
        )
        user = User.objects.get(pk=self.valid_user["id"])
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)


class TestCreateInvalidUser(APITestCase):
    invalid_user = {"email": "test@gmail.com", "username": "test@gmail.com"}

    def test_create_invalid_user(self):
        # serializer = CreateUserSerializer(data=self.invalid_user)

        response = self.client.post(
            reverse("signup"), data=self.invalid_user, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
