# Generated by Django 3.1.5 on 2021-09-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0010_auto_20210909_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(max_length=255),
        ),
    ]
