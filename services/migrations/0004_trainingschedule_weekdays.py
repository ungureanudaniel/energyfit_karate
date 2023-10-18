# Generated by Django 3.2.22 on 2023-10-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20231017_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=9)),
                ('day_ro', models.CharField(max_length=9, null=True)),
                ('day_en', models.CharField(max_length=9, null=True)),
                ('training1', models.CharField(max_length=100)),
                ('training1_ro', models.CharField(max_length=100, null=True)),
                ('training1_en', models.CharField(max_length=100, null=True)),
                ('training2', models.CharField(max_length=100)),
                ('training3', models.CharField(max_length=100)),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Training Schedule',
                'verbose_name_plural': 'Training Schedule',
            },
        ),
        migrations.CreateModel(
            name='WeekDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=9)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Week Days',
                'verbose_name_plural': 'Week Days',
            },
        ),
    ]
