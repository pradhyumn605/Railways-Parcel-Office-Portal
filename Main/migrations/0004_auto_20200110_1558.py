# Generated by Django 2.2.6 on 2020-01-10 10:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20200110_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='train_from_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 10, 10, 28, 14, 856289, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_to_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 10, 10, 28, 14, 856289, tzinfo=utc)),
        ),
    ]