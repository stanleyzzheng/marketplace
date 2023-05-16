from rest_framework.decorators import (
    api_view,
)

from rest_framework import status
from ..models import Cart, Item

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..serializers import CartSerializer


@api_view(["GET", "POST"])
def cart(request):
    if request.method == "GET":
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        pass
