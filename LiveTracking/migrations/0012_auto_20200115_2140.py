# Generated by Django 2.2.6 on 2020-01-15 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LiveTracking', '0011_auto_20200115_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livetracking',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 16, 10, 42, 200096, tzinfo=utc)),
        ),
    ]