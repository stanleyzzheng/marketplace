# Generated by Django 4.1.3 on 2023-06-01 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0012_alter_cartitem_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="price",
        ),
    ]