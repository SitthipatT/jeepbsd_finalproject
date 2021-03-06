# Generated by Django 3.1.13 on 2021-11-17 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fnl', '0006_auto_20211117_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displacement',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='displacement',
            name='route_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='displacement',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
