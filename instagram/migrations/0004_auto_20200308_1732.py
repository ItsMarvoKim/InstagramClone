# Generated by Django 4.0.5 on 2022-06-06 14:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_auto_20200307_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image_location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_photo'),
        ),
    ]
