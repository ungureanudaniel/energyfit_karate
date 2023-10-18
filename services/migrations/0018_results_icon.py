# Generated by Django 3.2.22 on 2023-10-18 19:50

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='icon',
            field=django_resized.forms.ResizedImageField(crop=None, default='a', force_format='WebP', keep_meta=True, quality=75, scale=0.5, size=[640, None], upload_to='results_icons'),
            preserve_default=False,
        ),
    ]