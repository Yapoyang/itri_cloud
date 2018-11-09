# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CctBar(models.Model):
    id = models.AutoField(primary_key=True)
    cct = models.TextField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cct_bar'


class CloudRestaurants(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'cloud_restaurants'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FreqComb(models.Model):
    cct = models.TextField(blank=True, null=True)
    lux = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'freq_comb'


class LuxBar(models.Model):
    id = models.AutoField(primary_key=True)
    lux = models.TextField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lux_bar'


class QXyplot(models.Model):
    id = models.AutoField(primary_key=True)
    demand = models.TextField(blank=True, null=True)
    q = models.TextField(blank=True, null=True)
    cct = models.TextField(blank=True, null=True)
    lux = models.TextField(blank=True, null=True)
    count = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q_xyplot'


class QusCct(models.Model):
    id = models.AutoField(primary_key=True)
    cct = models.TextField(blank=True, null=True)
    cold = models.FloatField(blank=True, null=True)
    feel = models.FloatField(blank=True, null=True)
    mind = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qus_cct'


class QusLux(models.Model):
    id = models.AutoField(primary_key=True)
    lux = models.TextField(blank=True, null=True)
    cold = models.FloatField(blank=True, null=True)
    feel = models.FloatField(blank=True, null=True)
    mind = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qus_lux'


class RestaurantsComment(models.Model):
    content = models.CharField(max_length=255)
    visitor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey('RestaurantsRestaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'restaurants_comment'


class RestaurantsFood(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    comment = models.CharField(max_length=50)
    is_spicy = models.IntegerField()
    restaurant = models.ForeignKey('RestaurantsRestaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'restaurants_food'


class RestaurantsRestaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'restaurants_restaurant'
