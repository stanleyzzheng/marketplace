from rest_framework import serializers
from .models import Item, Category, AppUser, CartItem, Cart
from rest_framework.authtoken.models import Token


# registration serializer
class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = AppUser(
            email=validated_data["email"],
            username=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = AppUser
        fields = ("id", "username", "password", "email")


# Login serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("id", "username", "password", "email")


# User serializer
class UserSerializer(serializers.ModelSerializer):
    # catalogs = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Catalog.objects.all()
    # )
    # items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    # cart = serializers.SlugRelatedField(slug_field="id", read_only=True)
    # cart = CartSerializer(read_only=True)

    class Meta:
        model = AppUser
        # fields = ("id", "username", "password", "email")
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source="*")
    # category = serializers.RelatedField(many=True, read_only=True)
    # category = CategorySerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source="owner.username")
    category = serializers.SlugRelatedField(
        slug_field="title", queryset=Category.objects.all()
    )

    class Meta:
        model = Item
        # fields = ("id", "title", "description", "category", "price")
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(
        many=True,
        read_only=True,
    )
    # items = serializers.SlugRelatedField(many=True, read_only=True)
    # items = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        # fields = ("id", "title", "description", "items")
        fields = "__all__"


class CartItemRetrieveSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "item", "quantity", "cart"]


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "cart_items"]


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "item", "quantity", "cart"]
