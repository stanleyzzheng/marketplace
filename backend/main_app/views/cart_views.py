from rest_framework.decorators import (
    api_view,
)

from rest_framework import status
from ..models import Cart, Item, CartItem

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..serializers import CartItemSerializer, CartSerializer


@api_view(["GET", "POST"])
def cart_items(request):
    token = request.COOKIES.get("token")
    if token is None:
        return Response(data={"failure": "failed, user is not logged in"})
    if request.method == "GET":
        user = Token.objects.get(key=token).user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)

        serializer = CartItemSerializer(cart_items, many=True)
        # cartserializer = CartSerializer(cart)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # return Response({"hello"})

    # elif request.method == "POST":
    #     serializer = CartItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
