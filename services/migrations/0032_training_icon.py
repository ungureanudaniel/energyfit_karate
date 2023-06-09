# Generated by Django 3.2.18 on 2023-04-30 11:57

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0031_training_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='icon',
            field=django_resized.forms.ResizedImageField(crop=None, default='b', force_format='WebP', keep_meta=True, quality=75, scale=0.5, size=[640, None], upload_to='training_types_icons'),
            preserve_default=False,
        ),
    ]
