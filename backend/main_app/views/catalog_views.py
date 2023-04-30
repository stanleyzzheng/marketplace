# from rest_framework.decorators import (
#     api_view,
#     permission_classes,
#     authentication_classes,
# )

# from rest_framework import status, permissions
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.response import Response


# from ..models import Catalog
# from ..serializers import CatalogSerializer

# Catalog views ####################################################


# @api_view(["GET"])
# def get_all_catalogs(request):
#     if request.method == "GET":
#         catalogs = Catalog.objects.all()
#         serializer = CatalogSerializer(catalogs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
# def catalogs(request):

#     if request.method == "POST":
#         serializer = CatalogSerializer(data=request.data)

#         if serializer.is_valid():
#             print("valid")
#             serializer.save(owner=request.user)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
