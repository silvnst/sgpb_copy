# Generated by Django 3.1.5 on 2021-08-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0004_remove_method_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
