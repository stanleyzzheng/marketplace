# Generated by Django 4.1.3 on 2023-05-14 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0008_cart_cartitem_cart_products"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="owner",
            new_name="user",
        ),
    ]
