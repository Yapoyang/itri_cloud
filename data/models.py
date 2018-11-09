# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LightTb(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.TextField(blank=True, null=True)
    gender = models.BigIntegerField(blank=True, null=True)
    cct = models.BigIntegerField(blank=True, null=True)
    cri = models.BigIntegerField(blank=True, null=True)
    lux = models.BigIntegerField(blank=True, null=True)
    caf = models.FloatField(blank=True, null=True)
    q = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    press = models.FloatField(db_column='Press', blank=True, null=True)  # Field name made lowercase.
    tm = models.FloatField(db_column='TM', blank=True, null=True)  # Field name made lowercase.
    rh = models.BigIntegerField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    precp = models.FloatField(db_column='Precp', blank=True, null=True)  # Field name made lowercase.
    humidity = models.BigIntegerField(blank=True, null=True)
    temp = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'light_tb'


class QuesTb(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.TextField(blank=True, null=True)
    gender = models.BigIntegerField(blank=True, null=True)
    st = models.BigIntegerField(blank=True, null=True)
    wt = models.BigIntegerField(blank=True, null=True)
    dos = models.BigIntegerField(db_column='DOS', blank=True, null=True)  # Field name made lowercase.
    insomnia = models.BigIntegerField(blank=True, null=True)
    slpqul = models.BigIntegerField(blank=True, null=True)
    nap = models.BigIntegerField(blank=True, null=True)
    naptime = models.BigIntegerField(blank=True, null=True)
    cafe = models.BigIntegerField(blank=True, null=True)
    tempam = models.BigIntegerField(blank=True, null=True)
    feelam = models.BigIntegerField(blank=True, null=True)
    mindam = models.BigIntegerField(blank=True, null=True)
    temppm = models.BigIntegerField(blank=True, null=True)
    feelpm = models.BigIntegerField(blank=True, null=True)
    mindpm = models.BigIntegerField(blank=True, null=True)
    q_time = models.TextField(blank=True, null=True)
    cct = models.BigIntegerField(blank=True, null=True)
    cri = models.BigIntegerField(blank=True, null=True)
    lux = models.BigIntegerField(blank=True, null=True)
    caf = models.FloatField(blank=True, null=True)
    q = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    press = models.FloatField(db_column='Press', blank=True, null=True)  # Field name made lowercase.
    tm = models.FloatField(db_column='TM', blank=True, null=True)  # Field name made lowercase.
    rh = models.BigIntegerField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    precp = models.FloatField(db_column='Precp', blank=True, null=True)  # Field name made lowercase.
    humidity = models.BigIntegerField(blank=True, null=True)
    temp = models.BigIntegerField(blank=True, null=True)
    time_block = models.TextField(db_column='time.block', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    class Meta:
      managed = False
      db_table = 'ques_tb'


class SleepTb(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.TextField(blank=True, null=True)
    gender = models.BigIntegerField(blank=True, null=True)
    st = models.BigIntegerField(blank=True, null=True)
    wt = models.BigIntegerField(blank=True, null=True)
    nap = models.BigIntegerField(blank=True, null=True)
    naptime = models.BigIntegerField(blank=True, null=True)
    cafe = models.BigIntegerField(blank=True, null=True)
    tempam = models.BigIntegerField(blank=True, null=True)
    feelam = models.BigIntegerField(blank=True, null=True)
    mindam = models.BigIntegerField(blank=True, null=True)
    temppm = models.BigIntegerField(blank=True, null=True)
    feelpm = models.BigIntegerField(blank=True, null=True)
    mindpm = models.BigIntegerField(blank=True, null=True)
    q_time = models.TextField(blank=True, null=True)
    dos = models.BigIntegerField(db_column='DOS', blank=True, null=True)  # Field name made lowercase.
    insomnia = models.BigIntegerField(blank=True, null=True)
    slpqul = models.BigIntegerField(blank=True, null=True)
    cct = models.BigIntegerField(blank=True, null=True)
    cri = models.BigIntegerField(blank=True, null=True)
    lux = models.BigIntegerField(blank=True, null=True)
    caf = models.FloatField(blank=True, null=True)
    q = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    press = models.FloatField(db_column='Press', blank=True, null=True)  # Field name made lowercase.
    tm = models.FloatField(db_column='TM', blank=True, null=True)  # Field name made lowercase.
    rh = models.BigIntegerField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    precp = models.FloatField(db_column='Precp', blank=True, null=True)  # Field name made lowercase.
    humidity = models.BigIntegerField(blank=True, null=True)
    temp = models.BigIntegerField(blank=True, null=True)
    time_block = models.TextField(db_column='time.block', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    class Meta:
      managed = False
      db_table = 'sleep_tb'

