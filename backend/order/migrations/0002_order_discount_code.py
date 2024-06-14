# Generated by Django 4.2.11 on 2024-06-13 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0001_initial"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="discount_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="discounts.discountcode",
            ),
        ),
    ]