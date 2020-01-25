# Generated by Django 2.2.6 on 2020-01-15 07:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20200115_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='tarin_live_station',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_from_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 15, 7, 17, 33, 92841, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_to_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 15, 7, 17, 33, 92841, tzinfo=utc)),
        ),
    ]