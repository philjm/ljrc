# Generated by Django 3.0.8 on 2020-08-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0012_auto_20200811_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpost',
            name='average',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
    ]
