# Generated by Django 3.1.5 on 2021-09-14 14:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praxismethoden', '0013_auto_20210909_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='content',
        ),
        migrations.AddField(
            model_name='method',
            name='tipp',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Hier noch ein Text, welcher als Tipp zur Methode angezeigt wird.', null=True, verbose_name='Tipp'),
        ),
        migrations.AlterField(
            model_name='method',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Der hier eingegebene Text beschreibt die Methode.', null=True, verbose_name='Beschreibung'),
        ),
    ]