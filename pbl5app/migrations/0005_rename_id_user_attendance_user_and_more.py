# Generated by Django 4.1.7 on 2023-05-06 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbl5app', '0004_listencode_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='listencode',
            old_name='id_user',
            new_name='user',
        ),
    ]
