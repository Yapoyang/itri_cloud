from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,render_to_response
from django.core import serializers
import json
import datetime
from post.models import sensor,con,er_test,av,oc,ab
import requests

def recv_data(request):
    if request.method =='POST':
       req=json.loads(request.body.decode('utf-8'))
       dat=sensor.objects.all()
       id_val=len(dat)+1
       device_val=req.get('device')
       value_val=req.get('value')
       DT_val=str(datetime.datetime.now())
       tb_insert_data=sensor(id=id_val,device=device_val,value=value_val,DT=DT_val)
       tb_insert_data.save()
       print(req)
       return JsonResponse('work',safe=False)
    else:
       return JsonResponse('wrong request',safe=False)

def show(request):
   if 'Lux' not in request.POST:
       tag=sensor.objects.filter(device=1)
       device1=[tag[i].device for i in range(len(tag))]
       value1 =[float(tag[i].value)  for i in range(len(tag))]
       DT1    =[tag[i].DT     for i in range(len(tag))]
       tag=sensor.objects.filter(device=2)
       device2=[tag[i].device for i in range(len(tag))]
       value2 =[float(tag[i].value)  for i in range(len(tag))]
       DT2    =[tag[i].DT     for i in range(len(tag))]
       tag=sensor.objects.filter(device=3)
       device3=[tag[i].device for i in range(len(tag))]
       value3 =[float(tag[i].value)  for i in range(len(tag))]
       DT3    =[tag[i].DT     for i in range(len(tag))]
       avg_value1=sum(value1)/len(value1)
       avg_value2=sum(value2)/len(value2)
       current_temp=value1[-1]
       current_humi=value2[-1]
       current_PIR =value3[-1]
       if current_PIR==0:
          PIR='vacant'
       else:
          PIR='occupied'
       cdt1=DT1[-1]
       cdt2=DT2[-1]
       cdt3=DT3[-1]
       #html='<html>Current Temperature : {a} °C -- {b}<br>Current Humidity : {c} % -- {d}<br>Area is {e} at {f}<br><br>Average Temperature : {g}<br>Average Humidity : {h}</html>'.format(a=current_temp,b=cdt1,c=current_humi,d=cdt2,e=PIR,f=cdt3,g=avg_value1,h=avg_value2)
       context={'a':current_temp,'b':cdt1,'c':current_humi,'d':cdt2,'e':PIR,'f':cdt3,'g':avg_value1,'h':avg_value2}
       return render_to_response('iot.html',context)

   if 'Lux' in request.POST:
       lux=request.POST['Lux']
       headers=json.dumps({'contenttype': 'application/json'})
       payload={'value':str(lux)}
       response = requests.post('http://52.198.25.52/load/',json.dumps(payload),headers)
       tag=sensor.objects.filter(device=1)
       device1=[tag[i].device for i in range(len(tag))]
       value1 =[float(tag[i].value)  for i in range(len(tag))]
       DT1    =[tag[i].DT     for i in range(len(tag))]
       tag=sensor.objects.filter(device=2)
       device2=[tag[i].device for i in range(len(tag))]
       value2 =[float(tag[i].value)  for i in range(len(tag))]
       DT2    =[tag[i].DT     for i in range(len(tag))]
       tag=sensor.objects.filter(device=3)
       device3=[tag[i].device for i in range(len(tag))]
       value3 =[float(tag[i].value)  for i in range(len(tag))]
       DT3    =[tag[i].DT     for i in range(len(tag))]
       avg_value1=sum(value1)/len(value1)
       avg_value2=sum(value2)/len(value2)
       current_temp=value1[-1]
       current_humi=value2[-1]
       current_PIR =value3[-1]
       if current_PIR==0:
          PIR='vacant'
       else:
          PIR='occupied'
       cdt1=DT1[-1]
       cdt2=DT2[-1]
       cdt3=DT3[-1]
       #html='<html>Current Temperature : {a} °C -- {b}<br>Current Humidity : {c} % -- {d}<br>Area is {e} at {f}<br><br>Average Temperature : {g}<br>Average Humidity : {h}</html>'.format(a=current_temp,b=cdt1,c=current_humi,d=cdt2,e=PIR,f=cdt3,g=avg_value1,h=avg_value2)
       context={'a':current_temp,'b':cdt1,'c':current_humi,'d':cdt2,'e':PIR,'f':cdt3,'g':avg_value1,'h':avg_value2}
       return render_to_response('iot.html',context)


def load_data(request):
    if request.method=='POST':
       req=json.loads(request.body.decode('utf-8'))
       id_val=len(con.objects.all())+1
       value_val=req.get('value')
       tb_insert_data=con(id=id_val,value=value_val)
       tb_insert_data.save()
       print(req)
       return JsonResponse('Work',safe=False)
    else:
       return JsonResponse('wrong request',safe=False)

def last(request):
    if request.method=='GET':
       req=con.objects.all()
       v=req[len(req)-1].value
       html='<html>new value = {a}'.format(a=v)
       return HttpResponse(html)

def findmachine(request):
    if request.method=='GET':
       req=er_test.objects.all()
       req_dict=er_test.toDict(req.count(),req)
       req_json=json.dumps(req_dict)
       req_out=json.loads(req_json)
       return JsonResponse(req_out,safe=False)

def pr(request):
    if request.method=='GET':
       req2=oc.objects.all()
       req2_dict=oc.toDict(req2.count(),req2)
       req2_json=json.dumps(req2_dict)
       req2_out=json.loads(req2_json)
       return JsonResponse(req2_out,safe=False)



