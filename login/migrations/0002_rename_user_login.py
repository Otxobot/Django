# Generated by Django 3.2.25 on 2024-08-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='login',
        ),
    ]
