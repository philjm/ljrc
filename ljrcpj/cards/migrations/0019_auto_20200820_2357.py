# Generated by Django 3.0.8 on 2020-08-20 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0018_auto_20200820_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpost',
            name='p9a',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='cardpost',
            name='p9c',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='cardpost',
            name='p9p',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='cardpost',
            name='p9t',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='cardpost',
            name='p9v',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
    ]
