# Generated by Django 3.1.7 on 2021-05-03 10:41

import datetime
import django.contrib.auth.models
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20210430_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='created_by',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=200),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='images',
            field=models.ImageField(default=datetime.datetime(2021, 5, 3, 10, 41, 57, 60200, tzinfo=utc), upload_to='media/'),
        ),
    ]