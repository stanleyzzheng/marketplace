from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)

from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from ..serializers import UserSerializer
from ..models import AppUser as User


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def users(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
