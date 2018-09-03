# Generated by Django 2.0.7 on 2018-09-03 01:56

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_auto_20180814_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDiplomaticRelation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('start_date', models.DateField(help_text='When this relation takes effect')),
                ('end_date', models.DateField(help_text='When this relation ceases to exist')),
                ('diplo_type', models.TextField(choices=[('A', 'Military Alliance'), ('D', 'Dual Monarchy'), ('M', 'Condominium'), ('T', 'Trade League'), ('W', 'At War'), ('CP', 'Client State - Puppet State'), ('CV', 'Client State - Vassal State'), ('CPU', 'Client State - Personal Union'), ('CCR', 'Client State - Colony - Royal'), ('CCP', 'Client State - Colony - Propreitary'), ('CCC', 'Client State - Colony - Charter')], default='CC', max_length=3)),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=150), size=None)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical diplomatic relation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(
            model_name='historicalnation',
            name='wikipedia',
        ),
        migrations.RemoveField(
            model_name='nation',
            name='wikipedia',
        ),
        migrations.AddField(
            model_name='diplomaticrelation',
            name='diplo_type',
            field=models.TextField(choices=[('A', 'Military Alliance'), ('D', 'Dual Monarchy'), ('M', 'Condominium'), ('T', 'Trade League'), ('W', 'At War'), ('CP', 'Client State - Puppet State'), ('CV', 'Client State - Vassal State'), ('CPU', 'Client State - Personal Union'), ('CCR', 'Client State - Colony - Royal'), ('CCP', 'Client State - Colony - Propreitary'), ('CCC', 'Client State - Colony - Charter')], default='CC', max_length=3),
        ),
        migrations.AddField(
            model_name='diplomaticrelation',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='When this relation ceases to exist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diplomaticrelation',
            name='first_party',
            field=models.ManyToManyField(related_name='first_parties', to='api.Nation'),
        ),
        migrations.AddField(
            model_name='diplomaticrelation',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=150), default='{test}', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diplomaticrelation',
            name='second_party',
            field=models.ManyToManyField(related_name='second_parties', to='api.Nation'),
        ),
        migrations.AddField(
            model_name='diplomaticrelation',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='When this relation takes effect'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalnation',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, default='{test}', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalnation',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=150), default='{test}', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalterritory',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=150), default='{test}', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nation',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, default='{test}', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nation',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=150), default='{test}', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='territory',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=150), default='{l}', size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalnation',
            name='control_type',
            field=models.TextField(blank=True, choices=[('CC', 'Complete Control'), ('DT', 'Disputed Territory')], default='CC', max_length=2),
        ),
        migrations.AlterField(
            model_name='nation',
            name='control_type',
            field=models.TextField(blank=True, choices=[('CC', 'Complete Control'), ('DT', 'Disputed Territory')], default='CC', max_length=2),
        ),
    ]
