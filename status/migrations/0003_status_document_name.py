# Generated by Django 4.1 on 2023-06-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_status_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='document_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
