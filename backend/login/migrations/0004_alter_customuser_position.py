# Generated by Django 4.2.11 on 2024-06-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0003_alter_customuser_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="position",
            field=models.CharField(default="user", max_length=20),
        ),
    ]