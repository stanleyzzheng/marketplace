from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Catalog, AppUser as User
from ..serializers import CatalogSerializer, CreateUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class TestCatalogView(APITestCase):
    def setUp(self) -> None:
        # createSerializer = CreateUserSerializer(data=self.test_user)

        # if createSerializer.is_valid():
        #     createSerializer.save()
        #     self.valid_user = createSerializer.data
        test_user = CreateUserSerializer(
            data={
                "email": "test@gmail.com",
                "username": "test@gmail.com",
                "password": "test123",
            }
        )
        # Create a valid user
        if test_user.is_valid():
            test_user.save()
            self.valid_user = User.objects.get(pk=test_user.data["id"])
            token = Token.objects.get(user=self.valid_user)
            self.client = APIClient()
            self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        for i in range(10):
            data = {"title": "catalog " + str(i)}
            serializer = CatalogSerializer(data=data)
            if serializer.is_valid():
                serializer.save(owner=self.valid_user)
                serializer.save()

    def test_get_all_catalogs(self):
        response = self.client.get(reverse("get_all_catalogs"))
        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.status_code, 200)

    def test_post_catalog(self):
        data = {"title": "catalog"}
        # serializer = CreateUserSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save(owner=self.valid_user)
        #     serializer.save()
        serializer = CatalogSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=self.valid_user)
            serializer.save()
        response = self.client.post(
            reverse("catalogs"), data=serializer.data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
