# Generated by Django 2.0 on 2017-12-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('cct', models.BigIntegerField(blank=True, null=True)),
                ('cri', models.BigIntegerField(blank=True, null=True)),
                ('lux', models.BigIntegerField(blank=True, null=True)),
                ('caf', models.FloatField(blank=True, null=True)),
                ('q', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'light',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QusAnd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('tempam', models.BigIntegerField(blank=True, null=True)),
                ('temppm', models.BigIntegerField(blank=True, null=True)),
                ('feelam', models.BigIntegerField(blank=True, null=True)),
                ('feelpm', models.BigIntegerField(blank=True, null=True)),
                ('mindam', models.BigIntegerField(blank=True, null=True)),
                ('mindpm', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'qus_and',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QusStat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('gender', models.BigIntegerField(blank=True, null=True)),
                ('sleeptime', models.BigIntegerField(blank=True, null=True)),
                ('awaketime', models.BigIntegerField(blank=True, null=True)),
                ('dos', models.BigIntegerField(blank=True, db_column='DOS', null=True)),
                ('hardsleep', models.BigIntegerField(blank=True, db_column='Hardsleep', null=True)),
                ('slpqua', models.BigIntegerField(blank=True, null=True)),
                ('nap', models.BigIntegerField(blank=True, null=True)),
                ('naptime', models.BigIntegerField(blank=True, null=True)),
                ('cafe', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'qus_stat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('press', models.FloatField(blank=True, db_column='Press', null=True)),
                ('tm', models.FloatField(blank=True, db_column='TM', null=True)),
                ('rh', models.BigIntegerField(blank=True, db_column='RH', null=True)),
                ('ws', models.FloatField(blank=True, db_column='WS', null=True)),
                ('wd', models.BigIntegerField(blank=True, db_column='WD', null=True)),
                ('precp', models.FloatField(blank=True, db_column='Precp', null=True)),
                ('humidity', models.BigIntegerField(blank=True, null=True)),
                ('temp', models.BigIntegerField(blank=True, null=True)),
                ('co2', models.BigIntegerField(blank=True, db_column='CO2', null=True)),
                ('time_block', models.TextField(blank=True, db_column='time.block', null=True)),
            ],
            options={
                'db_table': 'weather',
                'managed': False,
            },
        ),
    ]