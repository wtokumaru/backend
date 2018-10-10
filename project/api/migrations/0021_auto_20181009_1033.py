# Generated by Django 2.0.7 on 2018-10-09 17:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20181009_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalnation',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), default=[], help_text='Alternative names this state may be known by', size=None),
        ),
        migrations.AlterField(
            model_name='historicalnation',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='nation',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), default=[], help_text='Alternative names this state may be known by', size=None),
        ),
        migrations.AlterField(
            model_name='nation',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=[], size=None),
        ),
    ]
