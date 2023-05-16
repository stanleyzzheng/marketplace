from django.db import models
from django.contrib.auth.models import AbstractUser

# Auth token imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)


# Create your models here.
class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


# class Catalog(models.Model):
#     title = models.CharField(max_length=100, null=False)
#     description = models.CharField(max_length=100, blank=True)
#     owner = models.ForeignKey(
#         "AppUser", related_name="catalogs", on_delete=models.CASCADE
#     )


class Category(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, blank=True)

    # catalog = models.ForeignKey(
    #     "Catalog", related_name="categories", on_delete=models.CASCADE
    # )
    # def __str__(self) -> str:
    #     return self.title


class Item(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    category = models.ForeignKey(
        "Category", related_name="items", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/")
    owner = models.ForeignKey("AppUser", related_name="items", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Cart(models.Model):
    user = models.ForeignKey("AppUser", on_delete=models.CASCADE)
    items = models.ManyToManyField("Item", through="CartItem")

    def get_total_price(self):
        return sum(item.price for item in self.products.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
