# Generated by Django 3.1.5 on 2021-09-09 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0011_auto_20210909_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='file_url',
        ),
    ]
