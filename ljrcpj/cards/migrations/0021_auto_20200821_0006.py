# Generated by Django 3.0.8 on 2020-08-21 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0020_auto_20200821_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpost',
            name='p8h',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='cardpost',
            name='p9h',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='cardpost',
            name='rh',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
    ]
