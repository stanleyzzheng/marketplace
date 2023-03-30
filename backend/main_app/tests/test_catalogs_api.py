from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Catalog, AppUser as User
from ..serializers import CatalogSerializer


class TestCatalogView(APITestCase):

    test_catalog = {"title": "test shop"}
