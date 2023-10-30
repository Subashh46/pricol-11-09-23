# Generated by Django 4.1 on 2023-10-10 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0007_alter_status_machine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='machine',
            name='manufacture_year',
        ),
        migrations.AlterField(
            model_name='machine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.machine'),
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.plant')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='status.line'),
        ),
        migrations.AddField(
            model_name='machine',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='status.plant'),
        ),
    ]