# Generated by Django 3.1.13 on 2021-11-17 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fnl', '0009_delete_luckyday'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuckyDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rnk', models.IntegerField()),
                ('yearx', models.IntegerField()),
                ('monthx', models.IntegerField()),
                ('dayx', models.IntegerField()),
                ('datex', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
