# Generated by Django 3.0.8 on 2020-08-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_auto_20200811_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardpost',
            name='priceid',
        ),
        migrations.RemoveField(
            model_name='cardpost',
            name='priceurl',
        ),
        migrations.AddField(
            model_name='cardpost',
            name='printcount',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
    ]
