# Generated by Django 3.1.5 on 2021-09-09 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0012_auto_20210909_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_url',
            new_name='file',
        ),
    ]
