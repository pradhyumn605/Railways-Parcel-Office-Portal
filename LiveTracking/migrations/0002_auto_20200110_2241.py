# Generated by Django 2.0 on 2020-01-10 17:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LiveTracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livetracking',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 17, 11, 22, 510642, tzinfo=utc)),
        ),
    ]
