# Generated by Django 3.0.8 on 2020-08-20 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_cardpost_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardpost',
            old_name='printcount',
            new_name='serialnumbered',
        ),
    ]