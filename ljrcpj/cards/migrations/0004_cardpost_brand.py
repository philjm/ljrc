# Generated by Django 3.0.8 on 2020-08-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_cardpost_cardnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpost',
            name='brand',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
    ]
