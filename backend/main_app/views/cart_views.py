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
    user = request.user
    if request.method == "GET":
        cart = Cart.objects.get(user=user)
        print(cart)
        cart_items = CartItem.objects.filter(cart=cart)
        print(cart_items)
        serializer = CartItemSerializer(cart_items, many=True)
        # cartserializer = CartSerializer(cart)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "POST":
    #     serializer = CartItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
