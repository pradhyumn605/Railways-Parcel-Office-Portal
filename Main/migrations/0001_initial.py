# Generated by Django 2.2.6 on 2020-01-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.PositiveIntegerField()),
                ('train_from', models.CharField(max_length=50)),
                ('train_to', models.CharField(max_length=50)),
                ('station1', models.CharField(max_length=50)),
                ('station2', models.CharField(max_length=50)),
                ('station3', models.CharField(max_length=50)),
                ('station4', models.CharField(max_length=50)),
                ('station5', models.CharField(max_length=50)),
                ('station6', models.CharField(max_length=50)),
                ('station7', models.CharField(max_length=50)),
                ('station8', models.CharField(max_length=50)),
                ('station9', models.CharField(max_length=50)),
                ('station10', models.CharField(max_length=50)),
                ('station11', models.CharField(max_length=50)),
                ('station12', models.CharField(max_length=50)),
                ('station13', models.CharField(max_length=50)),
                ('station14', models.CharField(max_length=50)),
                ('station15', models.CharField(max_length=50)),
                ('station16', models.CharField(max_length=50)),
                ('station17', models.CharField(max_length=50)),
                ('station18', models.CharField(max_length=50)),
                ('station19', models.CharField(max_length=50)),
                ('station20', models.CharField(max_length=50)),
            ],
        ),
    ]
