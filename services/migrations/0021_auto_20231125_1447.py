# Generated by Django 3.2.22 on 2023-11-25 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_auto_20231125_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='No subject', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 14, 47, 26, 936742, tzinfo=utc)),
        ),
    ]
