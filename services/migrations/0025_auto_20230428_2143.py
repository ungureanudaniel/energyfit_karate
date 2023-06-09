# Generated by Django 3.2.18 on 2023-04-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_auto_20230428_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='experience_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='experience_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='experience_ro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='intro_de',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='intro_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='intro_ro',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill1_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill1_descr_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill1_descr_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill1_descr_ro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill1_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill1_ro',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill2_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill2_descr_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill2_descr_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill2_descr_ro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill2_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill2_ro',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill3_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill3_descr_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill3_descr_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill3_descr_ro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill3_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='skill3_ro',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
