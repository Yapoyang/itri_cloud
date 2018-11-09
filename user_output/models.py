# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CctBar(models.Model):
    cct = models.TextField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cct_bar'


class FreqComb(models.Model):
    cct = models.TextField(blank=True, null=True)
    lux = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'freq_comb'


class LuxBar(models.Model):
    lux = models.TextField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lux_bar'


class QXyplot(models.Model):
    demand = models.TextField(blank=True, null=True)
    q = models.TextField(blank=True, null=True)
    cct = models.TextField(blank=True, null=True)
    lux = models.TextField(blank=True, null=True)
    count = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_xyplot'


class QusCct(models.Model):
    cct = models.TextField(blank=True, null=True)
    cold = models.FloatField(blank=True, null=True)
    feel = models.FloatField(blank=True, null=True)
    mind = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qus_cct'


class QusLux(models.Model):
    lux = models.TextField(blank=True, null=True)
    cold = models.FloatField(blank=True, null=True)
    feel = models.FloatField(blank=True, null=True)
    mind = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qus_lux'
