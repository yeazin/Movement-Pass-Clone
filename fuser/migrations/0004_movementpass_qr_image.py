# Generated by Django 3.1.5 on 2021-05-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0003_auto_20210528_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementpass',
            name='qr_image',
            field=models.ImageField(null=True, upload_to='qr/'),
        ),
    ]