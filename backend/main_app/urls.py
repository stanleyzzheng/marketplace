from django.urls import path
from . import views

urlpatterns = [
    path("catalogs/", views.catalogs),
    path("categories/", views.categories),
    path("items/", views.items),
    path("categories/<int:pk>/", views.category_detail),
    path("items/<int:pk>/", views.item_detail),
    # Auth url's
    path("users/", views.users),
    path("signup/", views.sign_up_user),
    path("login/", views.loginUser),
    path("who_am_i/", views.who_am_i),
    path("logout/", views.logoutView),
]
