# Generated by Django 3.0.8 on 2020-08-19 23:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200804_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]