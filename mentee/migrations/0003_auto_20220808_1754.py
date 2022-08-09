# Generated by Django 3.2.13 on 2022-08-08 15:54

import cloudinary.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0002_config_mentee'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='profileImage',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='mentee',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, max_length=255),
        ),
    ]
