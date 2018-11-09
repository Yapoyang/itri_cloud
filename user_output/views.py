from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse, JsonResponse
#from user_output.models import Light, QusAnd, QusStat, Weather
from django.core import serializers
import time
import json

def overview2(request):
    if request.method=='GET':
       db_name=request.GET.get('db',None)
       tb_name=request.GET.get('tb',None)
       id = request.GET.get('id',None)
       if tb_name=='light':
             temp_tb=Light
       elif tb_name=='qusans':
             temp_tb=QusAnd
       elif tb_name=='qusstat':
             temp_tb=QusStat
       elif tb_name=='weather':
             temp_tb==Weather
       else:
             return JsonRespnse('Wrong table name',safe=False)
       if id:
             if id=='all':
                try:
                       tag=temp_tb.objects.using(db_name).all()
                except temp_tb.DoesNotExist:
                       return JsonResponse('Fail1',safe=False)
                else:
                       dat=serializers.serialize('json',tag)
                       return JsonResponse(dat,safe=False)
             elif id.isdigit():
                try:
                       tag=temp_tb.objects.using(db_name).get(pk=id)
                except temp_tb.DoesNotExist:
                       dat={'warning':'do not exist'}
                       return JsonResponse(dat,safe=False)
                else:
                       dat=serializers.serialize('json',[tag,])
                       return JsonResponse(dat,safe=False)
             else:
                return JsonResponse('wrong id request',safe=False)
