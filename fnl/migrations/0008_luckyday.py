# Generated by Django 3.1.13 on 2021-11-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnl', '0007_auto_20211117_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuckyDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('year', models.DateField()),
                ('month', models.DateField()),
                ('day', models.DateField()),
            ],
        ),
    ]
