# Generated by Django 4.1.3 on 2023-05-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0005_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(upload_to="media/images/"),
        ),
    ]