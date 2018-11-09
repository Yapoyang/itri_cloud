from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse
from data.models import QuesTb, LightTb, SleepTb
from django.http import JsonResponse
from django.core import serializers
import time
import json

def overview(request):
    if request.method=='GET':
       id = request.GET.get('id',None)
       tb=request.GET.get('tb',None)
       if tb=='ques':
          temptb=QuesTb
       elif tb=='light':
          temptb=LightTb
       elif tb=='sleep':
          temptb=SleepTb
       else:
          return JsonResponse('Unknown table',safe=False)
       if id:
             if id=='all':
                   try:
                          tag=temptb.objects.using('itri_db_01').all()
                   except temptb.DoesNotExist:
                          return JsonResponse("Fail",safe=False)
                   else:
                          dat=serializers.serialize('json',tag)
                         #return JsonResponse(tag)
                          return JsonResponse(dat,safe=False)
             elif id.isdigit():
                   try:
                          tag=temptb.objects.using('itri_db_01').get(pk=id)
                   except temptb.DoesNotExist:
                          dat={'warning':'do not exist'}
                          return JsonRespones(dat,safe=False)
                   else:
                          dat=serializers.serialize('json',[tag,])
                          return JsonResponse(dat,safe=False)
             else:
                   return JsonResponse('second fail',safe=False)
            
       else:
             return JsonResponse('third fail',safe=False)

def loaddata(request):
    if request.method=='GET':
       try:
            latest_id=QuesTb.objects.latest('id')
            user_id=request.GET['user_id']
            cct=request.GET['cct']
            lux=request.GET['lux']
            cri=request.GET['cri']
            caf=request.GET['caf']
            q=request.GET['q']
            QuesTb.objects.create(
               id=latest_id.id+1, user_id=user_id,
               cct=cct,cri=cri,lux=lux,caf=caf,q=q)
       except MultiValueDictKeyError:
            return JsonResponse('Error:Missing value exist',safe=False)
       else:
            return JsonResponse('sucssess, load No.{} instance'.format(latest_id.id+1),safe=False)
    else:
       return JsonResponse('wrong request',safe=False)

def revisedata(request):
    if request.method=='GET':
       request_id=request.GET.get('id',None)
       user_id=request.GET['user_id']
       cct=request.GET['cct']
       lux=request.GET['lux']
       cri=request.GET['cri']
       caf=request.GET['caf']
       q=request.GET['q']
       QuesTb.objects.filter(id=request_id).update(
          user_id=user_id,cct=cct,cri=cri,lux=lux,caf=caf,q=q)
       return JsonResponse('success, revise No.{} instance'.format(request_id),safe=False)
    else:
       return JsonResponse('wrong request',safe=False)

def deletedata(request):
    if request.method=='GET':
       request_id=request.GET.get('id',None)
       deleted_data=QuesTb.objects.get(id=request_id)
       deleted_data.delete()
       response='Success, No.{} instance deleted'.format(request_id)
       return JsonResponse(response,safe=False)
    class Meta:
        managed = False
        db_table = 'django_migrations'




