# Generated by Django 3.1.5 on 2021-05-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0003_auto_20210503_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementpass',
            name='traking_id',
            field=models.IntegerField(null=True),
        ),
    ]
