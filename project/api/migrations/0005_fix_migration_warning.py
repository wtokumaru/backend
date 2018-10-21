# Generated by Django 2.1.2 on 2018-10-18 22:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181011_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), default=list, help_text='Alternative names this state may be known by', size=None),
        ),
        migrations.AlterField(
            model_name='entity',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='historicalentity',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), default=list, help_text='Alternative names this state may be known by', size=None),
        ),
        migrations.AlterField(
            model_name='historicalentity',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='historicalpoliticalentity',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), default=list, help_text='Alternative names this state may be known by', size=None),
        ),
        migrations.AlterField(
            model_name='historicalpoliticalentity',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None),
        ),
    ]