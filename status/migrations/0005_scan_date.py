# Generated by Django 4.1 on 2023-09-11 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_scan'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='date',
            field=models.CharField(default=datetime.date(2023, 9, 11), max_length=255),
            preserve_default=False,
        ),
    ]