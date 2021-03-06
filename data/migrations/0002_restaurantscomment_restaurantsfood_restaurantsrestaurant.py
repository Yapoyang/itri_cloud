# Generated by Django 2.0 on 2017-12-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('visitor', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'restaurants_comment',
            },
        ),
        migrations.CreateModel(
            name='RestaurantsFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=0, max_digits=3)),
                ('comment', models.CharField(max_length=50)),
                ('is_spicy', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'restaurants_food',
            },
        ),
        migrations.CreateModel(
            name='RestaurantsRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'restaurants_restaurant',
            },
        ),
    ]
