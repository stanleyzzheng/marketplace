# Generated by Django 4.1.3 on 2023-01-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_alter_category_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
