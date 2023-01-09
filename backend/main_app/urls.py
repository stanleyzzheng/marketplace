from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.categories),
    path("items/", views.items),
    path("categories/<int:pk>/", views.category_detail),
    path("items/<int:pk>/", views.item_detail),
    path("users/", views.Users),
    path("signup/", views.sign_up_user),
    path("login/", views.loginUser),
]
