# Generated by Django 3.0.8 on 2020-08-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20200810_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpost',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/cards/03-04-Bowman-LeBron.jpg', null=True, upload_to='images'),
        ),
    ]
