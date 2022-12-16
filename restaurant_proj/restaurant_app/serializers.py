from rest_framework import serializers
from .models import Item, Category, AppUser


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("id", "username", "password", "email")

    def create(self, validated_data):
        user = AppUser(
            email=validated_data["email"],
            username=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


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
        fields = ("id", "title", "description", "items")


# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=100)
#     description = serializers.CharField(required=False, max_length=250)
#     # category = serializers.RelatedField(
#     #     source="category.title", queryset=Category.objects.all()
#     # )
#     category = serializers.CharField(source="category.title")

#     def create(self, validated_data):
#         return Item.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.category = validated_data.get("category", instance.category)
#         instance.save()


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=100)
#     description = serializers.CharField(required=False, max_length=250)
#     items = serializers.CharField()
#     # items = serializers.RelatedField(
#     #     source="category.items", queryset=Item.objects.filter(category=title)
#     # )

#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.save()
