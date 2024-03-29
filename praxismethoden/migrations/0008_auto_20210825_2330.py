# Generated by Django 3.1.5 on 2021-08-25 21:30

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0007_method_file_raw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='file_raw',
            field=models.FileField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='raw/', verbose_name='Dokument'),
        ),
    ]
