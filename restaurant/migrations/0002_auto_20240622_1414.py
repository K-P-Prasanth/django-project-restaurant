# Generated by Django 2.1.5 on 2024-06-22 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='vegBoll',
            new_name='vegBool',
        ),
    ]
