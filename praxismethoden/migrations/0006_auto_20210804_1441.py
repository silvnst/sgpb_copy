# Generated by Django 3.1.5 on 2021-08-04 12:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0005_auto_20210803_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='files',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='method',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
