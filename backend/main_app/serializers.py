from rest_framework import serializers
from .models import Item, Category, AppUser, Catalog
from rest_framework.authtoken.models import Token


# class UserSerializer(serializers.ModelSerializer):
#     # username = serializers.EmailField(source="email")
#     # print(username)

#     class Meta:
#         model = AppUser
#         fields = ("id", "username", "password", "email")

# def create(self, validated_data):
#     user = AppUser(
#         email=validated_data["email"],
#         username=validated_data["email"],
#     )
#     user.set_password(validated_data["password"])
#     user.save()
#     return user

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
    catalogs = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Catalog.objects.all()
    )

    class Meta:
        model = AppUser
        fields = ("id", "username", "password", "email", "catalogs")


class ItemSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source="*")
    # category = serializers.RelatedField(many=True, read_only=True)
    # category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ("id", "title", "description", "category", "price")


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


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"

    owner = serializers.ReadOnlyField(source="owner.username")
    categories = CategorySerializer(many=True, read_only=True)
    # categories = serializers.SerializerMethodField()

    # def get_categories(self, obj):
    #     return CategorySerializer(obj.categories).data
