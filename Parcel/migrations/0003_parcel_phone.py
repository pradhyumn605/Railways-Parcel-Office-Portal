# Generated by Django 2.2.6 on 2020-01-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parcel', '0002_auto_20200115_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='phone',
            field=models.CharField(default=1234567890, max_length=13),
            preserve_default=False,
        ),
    ]