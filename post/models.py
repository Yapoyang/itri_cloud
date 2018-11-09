from django.db import models
from collections import OrderedDict
class sensor(models.Model):
    id=models.AutoField(primary_key=True)
    device=models.CharField(max_length=200)
    value= models.CharField(max_length=200)
    DT=models.CharField(max_length=200)
    class Meta:
        managed=False
        db_table='sensor'

class con(models.Model):
      id=models.AutoField(primary_key=True)
      value=models.CharField(max_length=200)
      class Meta:
          managed=False
          db_table='test'


class er_test(models.Model):
      id=models.AutoField(primary_key=True)
      name=models.CharField(max_length=200)
      macid=models.CharField(max_length=200)
      loc=models.CharField(max_length=200)
      class Meta:
          managed=False
          db_table='er_test'
      def toDict(count,tag):
          dict_tag=OrderedDict()
          ls_member=[]
          i=0
          while i<count:
                  dict_member=OrderedDict()
                  dict_member['id']=tag[i].id
                  dict_member['name']=tag[i].name
                  dict_member['macid']=tag[i].macid
                  dict_member['loc']=tag[i].loc
                  ls_member.append(dict_member)
                  i+=1
          dict_tag['member']=ls_member
          return dict_tag

class av(models.Model):
      id=models.AutoField(primary_key=True)
      bed=models.CharField(max_length=200)
      room=models.CharField(max_length=200)
      class Meta:
          managed=False
          db_table='availableroom'
      def toDict(count,tag):
          dict_tag=OrderedDict()
          ls_member=[]
          i=0
          while i<count:
                  dict_member=OrderedDict()
                  dict_member['id']=tag[i].id
                  dict_member['bed']=tag[i].bed
                  dict_member['room']=tag[i].room
                  ls_member.append(dict_member)
                  i+=1
          dict_tag['count']=count
          dict_tag['member']=ls_member
          return dict_tag


class oc(models.Model):
      id=models.AutoField(primary_key=True)
      bed=models.CharField(max_length=200)
      room=models.CharField(max_length=200)
      time=models.CharField(max_length=200)
      class Meta:
          managed=False
          db_table='occupiedroom'
      def toDict(count,tag):
          dict_tag=OrderedDict()
          ls_member=[]
          i=0
          while i<count:
                  dict_member=OrderedDict()
                  dict_member['iv']=tag[i].bed
                  dict_member['room']=tag[i].room
                  dict_member['status']=tag[i].time
                  ls_member.append(dict_member)
                  i+=1
          dict_tag['member']=ls_member
          return dict_tag

class ab(models.Model):
      id=models.AutoField(primary_key=True)
      bed=models.CharField(max_length=200)
      room=models.CharField(max_length=200)
      status=models.CharField(max_length=200)
      class Meta:
          managed=False
          db_table='abnormalroom'
      def toDict(count,tag):
          dict_tag=OrderedDict()
          ls_member=[]
          i=0
          while i<count:
                  dict_member=OrderedDict()
                  dict_member['id']=tag[i].id
                  dict_member['bed']=tag[i].bed
                  dict_member['room']=tag[i].room
                  dict_member['status']=tag[i].status
                  ls_member.append(dict_member)
                  i+=1
          dict_tag['count']=count
          dict_tag['member']=ls_member
          return dict_tag

