# Generated by Django 3.0.8 on 2020-08-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20200810_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpost',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images'),
        ),
    ]
