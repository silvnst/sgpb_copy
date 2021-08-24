# Generated by Django 3.1.5 on 2021-08-24 11:21

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='file_raw',
            field=models.ImageField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='raw/'),
        ),
    ]