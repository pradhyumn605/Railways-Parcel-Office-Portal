# Generated by Django 2.2.6 on 2020-02-20 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20200220_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='train_from_time',
            field=models.TimeField(default=datetime.datetime(2020, 2, 20, 17, 3, 46, 872731, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_to_time',
            field=models.TimeField(default=datetime.datetime(2020, 2, 20, 17, 3, 46, 872731, tzinfo=utc)),
        ),
    ]
