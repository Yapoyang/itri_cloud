from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse, JsonResponse
from personal.models import CctBar,LuxBar,QXyplot,QusCct,QusLux
from django.core import serializers
import time 
import json
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine

def plotdata(request):
    if request.method=='GET':
       db_name=request.GET.get('db',None)
       tb_name=request.GET.get('tb',None)
       if tb_name=='cctbar':
             temp_tb=CctBar
       elif tb_name=='luxbar':
             temp_tb=LuxBar
       elif tb_name=='qxyplot':
             temp_tb=QXyplot
       elif tb_name=='quscct':
             temp_tb=QusCct
       elif tb_name=='quslux':
             temp_tb=QusLux

       else:
            return JsonResponse('Wrong table name',safe=False)
       tag=temp_tb.objects.using(db_name).all()
       dat=serializers.serialize('json',tag)
       db = MySQLdb.connect(host="52.198.25.52",user="yapo", passwd="itrieosl", db="itri_db_01")
       start="SELECT * FROM itri_db_01.light_tb"
       data=pd.read_sql(start,db)
       db.close()
       def cct_count(x):
           if type(x[0])==type(''):
              cct_index=["3000",'3500','4000','4500','5000','6000']
              count=[x[x==tag].shape[0] for tag in cct_index] 
              out=pd.DataFrame({'id':list(range(1,7)),'cct':cct_index,'count':count})
              out=out[['id','cct','count']]
              return(out)
           else:
              cct_index=[3000,3500,4000,4500,5000,6000]
              count=[x[x==tag].shape[0] for tag in cct_index]
              out=pd.DataFrame({'id':list(range(1,7)),'cct':cct_index,'count':count})
              out=out[['id','cct','count']]
              return(out)
       def lux_count(x):
           if type(x[0])==type(''):
              lux_index=["200",'400','600','800','1000']
              count=[x[x==tag].shape[0] for tag in lux_index]
              out=pd.DataFrame({'id':list(range(1,6)),'lux':lux_index,'count':count})
              out=out[['id','cct','count']]
              return(out)
           else:
              lux_index=[200,400,600,800,1000]
              count=[x[x==tag].shape[0] for tag in lux_index]
              out=pd.DataFrame({'id':list(range(1,6)),'lux':lux_index,'count':count})
              out=out[['id','lux','count']]
              return(out)
       def comb_count(data):
           lux_max=pd.crosstab(data['cct'],data['lux']).apply(max)
           cct_max=pd.crosstab(data['cct'],data['lux']).apply(max,axis=1)
           lux_max_tag=lux_max[lux_max==max(lux_max)].index[0]
           cct_max_tag=cct_max[cct_max==max(cct_max)].index[0]
           count=max(lux_max)
           return([cct_max_tag,lux_max_tag,count]) 
       id_tag=data.user_id.unique()
       tag=id_tag[0]
       for tag in id_tag:
           tag_s=tag.split(':',6) 
           tag_comb=''
           for a in tag_s: tag_comb+=a #user_id變成沒有冒號
           db_name=tag_comb          
           temp_data=data[data['user_id']==tag]
           tbcct=cct_count(temp_data.cct)
           tblux=lux_count(temp_data.lux)
           freq_comb=pd.DataFrame([comb_count(temp_data)[:2]],columns=['cct','lux'])
           engine = create_engine("mysql://yapo:itrieosl@52.198.25.52/"+db_name)
           tbcct.to_sql('cct_bar', engine, if_exists='replace',index=False)
           tblux.to_sql('lux_bar', engine, if_exists='replace',index=False)
           freq_comb.to_sql('freq_comb', engine, if_exists='replace',index=False)
       return JsonResponse(dat,safe=False)

