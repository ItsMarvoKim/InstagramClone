# Generated by Django 4.0.5 on 2022-06-06 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20200308_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
