from rest_framework.decorators import (
    api_view,
)

from rest_framework import status

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..serializers import CreateUserSerializer
from django.contrib.auth import authenticate

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
