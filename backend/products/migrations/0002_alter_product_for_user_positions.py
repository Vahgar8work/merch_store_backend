# Generated by Django 4.2.11 on 2024-06-26 10:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='for_user_positions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=6), default=list, help_text='comma separated list: MB - member, CR - Core, JS - Joint Sec, FS - Finance Sec, GS - Gen Sec. Ex: GS,FS,JS,CR', size=6),
        ),
    ]
