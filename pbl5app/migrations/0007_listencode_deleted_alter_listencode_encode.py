# Generated by Django 4.1.7 on 2023-05-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbl5app', '0006_remove_attendance_user_remove_listencode_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listencode',
            name='deleted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listencode',
            name='encode',
            field=models.TextField(blank=True, null=True),
        ),
    ]
