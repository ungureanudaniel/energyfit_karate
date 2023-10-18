# Generated by Django 3.2.22 on 2023-10-18 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_trainingschedule_weekdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingschedule',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.weekdays'),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='day_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.weekdays'),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='day_ro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.weekdays'),
        ),
    ]
