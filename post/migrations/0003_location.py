# Generated by Django 2.0 on 2018-09-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_con'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('macid', models.CharField(max_length=200)),
                ('loc', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'er_test',
                'managed': False,
            },
        ),
    ]