# Generated by Django 2.2.6 on 2020-01-15 06:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_auto_20200114_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='train_from_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 15, 6, 50, 23, 662596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_to_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 15, 6, 50, 23, 662596, tzinfo=utc)),
        ),
    ]