from django.urls import path
from . import views

urlpatterns = [
    path("catalogs/", views.catalogs, name="catalogs"),
    path("allcatalogs/", views.get_all_catalogs, name="get_all_catalogs"),
    path("categories/", views.categories),
    path("items/", views.items),
    path("categories/<int:pk>/", views.category_detail),
    path("items/<int:pk>/", views.item_detail),
    # Auth url's
    path("users/", views.users),
    path("users/<int:pk>/", views.user_detail, name="user_detail"),
    path("signup/", views.sign_up_user, name="signup"),
    path("login/", views.loginUser),
    path("who_am_i/", views.who_am_i),
    path("logout/", views.logoutView),
]
