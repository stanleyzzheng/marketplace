from django.shortcuts import render
from rest_framework import status

# from django.http import HttpResponse, JsonResponse
from .models import Item, Category, AppUser as User
from rest_framework.decorators import api_view
from .serializers import (
    CategorySerializer,
    ItemSerializer,
    UserSerializer,
)
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout


# Create your views here.


# def send_the_homepage(request):
#     print("home")
#     theIndex = open("static/index.html").read()
#     return HttpResponse(theIndex)


@api_view(["POST"])
def sign_up_user(request):
    if request.method == "POST":
        # print(request.data)
        # username = request.data["username"]
        email = request.data["email"]
        # request.data["username"] = email

        # password = request.data["password"]
        # new_user = User.objects.create_user(username=email, password=password, email=email)
        # new_user = User.objects.create_user(username=email, password=password, email=email)
        # return Response({"created": "True"}, status=status.HTTP_201_CREATED)
        request.data["username"] = email
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)

            serializer.save()
            # serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # print(new_user)
    # # new_user = User.objects.create_user(username, email, password)
    # print(request.data)


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        email = request.data["email"]
        password = request.data["password"]
        serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():

        # user = authenticate(username=email, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return Response()


@api_view(["GET", "POST"])
def Users(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def category(request):
    if request.method == "GET":
        categories = Category.objects.all().values()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
        # print(categories)
        # return JsonResponse({"categories": list(categories)}, status=200)
        # print(serializer.get_field_names)

    elif request.method == "POST":
        # try:

        #     title = request.data["title"]
        #     print(title)
        #     print(request.data)
        #     new_category = Category.objects.create(title=title)
        #     tmpJson = serializers.serialize("json", new_category)
        #     tmpObj = json.loads(tmpJson)
        #     return JsonResponse(json.dumps(tmpObj), safe=False)
        # except:
        #     return JsonResponse("failed to create Category", status=400)

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


#


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
