# Generated by Django 3.2.22 on 2023-10-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_rename_day_weekdays_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingschedule',
            name='day',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='day_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='day_ro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='WeekDays',
        ),
    ]