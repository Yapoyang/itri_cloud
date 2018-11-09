from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View,TemplateView

def here(request):
    return HttpResponse('yo, mother fucker')

def add(request,a,b):
    s=int(a)+int(b)
    return HttpResponse([str(s),',mother fucker!'])

#def math(request,a,b):
 #   a=int(a);b=int(b)
  #  s=a+b;d=a-b;p=a*b;q=a/b
    #t=get_template('math.html')
    #c=template.Context({'s':s,'d':d,'p':p,'q':q})
    #return render_to_response('math.html',locals())


def menu(request):
    food1={'names':'mother','price':60,'comment':'fucker','is_spicy':True}
    food2={'names':'samlj','price':60,'comment':'fucker','is_spicy':True}
    foods=[food1,food2]
    return render_to_response('menu.html',locals())


def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] !='':
        return HttpResponse('Welcome! Bad Mother Fucker~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def use_session(request):
    request.session['lucky_number']=8
    if 'lucky_number' in request.session:
        lucky_number=request.session['lucky_number']
        response=HttpResponse('Your lucky_number is '+lucky_number)
    del request.session['lucky_number']
    return response

def session_test(request):
    sid=request.COOKIES['sessionid']
    sid2=request.session.session_key
    s=Session.objects.get(pk=sid)
    s_info=('Session ID:'+sid+
           '<br>SessionID2:'+sid2+
           '<br>Expire_date'+str(s.expire_date)+
           '<br>Data:'+str(s.get_decoded()))
    return HttpResponse(s_info)

def login(request):
    
    if request.user.is_authenticated():
       return HttpResponseRedirect('/index/')

    username=request.POST.get('username','')
    password=request.POST.get('password','')

    user=auth.authenticate(username=username,password=password)

    if user is not None and user.is_active:
         auth.login(request,user)
         return HttpResponseRedirect('/index/')
    else:
         return render_to_response('login.html',locals())
         #return render_to_response('login.html',RequestContext(request,locals())) 

class IndexView(TemplateView):
      template_name='index1.html'
      def get(self, request, *args, **kwargs):
          context=self.get_context_data(**kwargs)
          context['request']=request
          return self.render_to_response(context)

def index(request):
    return render_to_response('index.html',locals())
    #return render_to_response('index.html',RequestContext(request,locals()))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
       form=UserCreationForm()
    return render_to_response('register.html',locals())

class HereView(View):
      def get(self,request):
          return HttpResponse('Yo, mother fuckers!')

