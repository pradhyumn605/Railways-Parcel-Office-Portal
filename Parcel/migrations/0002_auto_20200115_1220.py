# Generated by Django 2.2.6 on 2020-01-15 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parcel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parcel',
            options={'verbose_name_plural': 'Parcel'},
        ),
        migrations.RenameField(
            model_name='parcel',
            old_name='reciver_adhar',
            new_name='reciever_adhar',
        ),
        migrations.RenameField(
            model_name='parcel',
            old_name='reciver_name',
            new_name='reciever_name',
        ),
    ]