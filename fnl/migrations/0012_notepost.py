# Generated by Django 3.1.13 on 2021-11-18 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fnl', '0011_delete_displacement'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_good_day', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=500)),
                ('date_rec', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]