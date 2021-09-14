# Generated by Django 3.1.5 on 2021-09-01 13:11

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0008_auto_20210825_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='file',
        ),
        migrations.RemoveField(
            model_name='method',
            name='file_raw',
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='raw/', verbose_name='Dokument')),
                ('method', models.ManyToManyField(related_name='method_files', to='praxismethoden.Method')),
            ],
        ),
    ]
