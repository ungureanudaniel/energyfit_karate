# Generated by Django 3.2.22 on 2023-10-18 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20231018_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weekdays',
            old_name='day',
            new_name='name',
        ),
    ]
