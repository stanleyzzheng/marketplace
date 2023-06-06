from rest_framework.decorators import (
    api_view,
)

from rest_framework import status
from ..models import Cart, Item, CartItem

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..serializers import (
    CartItemRetrieveSerializer,
    CartItemCreateSerializer,
)


@api_view(["GET", "POST", "PUT"])
def cart_items(request):
    token = request.COOKIES.get("token")
    if token is None:
        return Response(data={"failure": "user is not logged in"})
    user = Token.objects.get(key=token).user
    cart = Cart.objects.get(user=user)
    if request.method == "GET":
        cart_items = CartItem.objects.filter(cart=cart)

        serializer = CartItemRetrieveSerializer(cart_items, many=True)
        # cartserializer = CartSerializer(cart)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        request.data["cart"] = cart.id
        print(request.data)
        serializer = CartItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({"failed"}, status=status.HTTP_400_BAD_REQUEST)

    # return Response({"hello"})

    # elif request.method == "POST":
    #     serializer = CartItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
