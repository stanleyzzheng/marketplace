from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Catalog
from ..serializers import CatalogSerializer


class TestGetCatalogDetail(APITestCase):

    test_catalog = {}
