# Generated by Django 3.2.22 on 2023-11-25 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_auto_20231125_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 14, 53, 16, 813705, tzinfo=utc)),
        ),
    ]