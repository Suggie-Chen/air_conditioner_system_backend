# Generated by Django 3.0.3 on 2020-05-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200527_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targettemplog',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='windlog',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
