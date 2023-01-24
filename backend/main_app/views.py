from django.shortcuts import render
from rest_framework import status, permissions
from django.middleware import csrf

# from django.http import HttpResponse, JsonResponse
from .models import Item, Category, AppUser as User, Catalog

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)

from .serializers import (
    CategorySerializer,
    ItemSerializer,
    UserSerializer,
    CatalogSerializer,
    CreateUserSerializer,
    LoginSerializer,
)

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

# from django.core import serializers
import json

# Create your views here.

# Authentication / Registration Views
@api_view(["POST"])
def sign_up_user(request):
    if request.method == "POST":

        request.data["username"] = request.data["email"]
        # password = request.data["password"]
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)

            serializer.save()
            # serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def loginUser(request):
    if request.method == "POST":
        user = authenticate(
            username=request.data["email"], password=request.data["password"]
        )
        print(user)
        if user is not None:
            token = Token.objects.get(user=user)
            response = Response()
            response.set_cookie(
                key="token", value=token.key, httponly=True, secure=True
            )
            data = {"token": "Token " + token.key, "user": user.username}
            response.data = {"Success": "Login successfully", "data": data}
            response.status = status.HTTP_200_OK
            return response
            # return Response(user)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# whoami view for auth
@api_view(["GET"])
def who_am_i(request):
    if request.method == "GET":
        # print(request.META.get("HTTP_AUTHORIZATION"))
        # print(request.COOKIES.get("token"))

        # create response object
        response = Response()

        # create token object
        token = request.COOKIES.get("token")
        print(token)
        # validate token and find user
        if token is not None and token != "logged out":
            user = Token.objects.get(key=token).user
            print(user)
            # create data
            data = {"token": "Token " + token, "user": user.username}

            response.data = data
            response.status = status.HTTP_200_OK
            return response

        # send Response with request.data attached.
        return Response(data={"success": "failed, user is not logged in"})


# logout view
@api_view(["POST"])
def logoutView(request):
    if request.method == "POST":
        response = Response()
        response.delete_cookie("token")
        response.data = {"Success": "Logged out successfully"}
        return response


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def Users(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# Catalog views ####################################################
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def catalogs(request):
    if request.method == "GET":
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CatalogSerializer(data=request.data)

        if serializer.is_valid():
            print("valid")
            serializer.save(owner=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Category Views ####################################################
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  Item Views ####################################################


@api_view(["GET", "POST"])
def items(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response


@api_view(["GET", "PUT", "DELETE"])
def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
