# Generated by Django 3.2.22 on 2024-11-22 22:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_auto_20231125_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 22, 22, 5, 9, 353993, tzinfo=utc)),
        ),
    ]
