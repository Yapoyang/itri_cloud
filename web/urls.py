"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


admin.autodiscover()
from web.views import welcome,session_test,register,IndexView,index
from restaurants.views import  menu, list_restaurants,comment,list,list_users
import restaurants
from post.views import recv_data,show,load_data,last,findmachine,pr
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
from web import views
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from data.views import overview #loaddata,revisedata, deletedata
#from user_output.views import overview2
from personal.views import plotdata
from django.urls import path




#urlpatterns = [
#    path('admin/', admin.site.urls),
#]
urlpatterns =[
    url(r'^$',index),
    url(r'^admin/',admin.site.urls),
    #url(r'^menu/(\d{1,5})/$',menu),
    url(r'^menu/(?P<pk>\d+)/$',restaurants.views.MenuView.as_view()),
    #url(r'^menu/(?P<pk>\d+)/$',DetailView.as_view(template_name='menu.html')),  #not template view
    url(r'^welcome/$',welcome),
    #url(r'^restaurants_list/$',list_restaurants),
    url(r'^restaurants_list/$',login_required(restaurants.views.RestaurantsView.as_view())),
    #url(r'^restaurants_list/$',login_required(TemplateView.as_view(template_name='restaurants_list.html'))),
    url(r'^users_list/$',list_users),
    #url(r'^comment/(?P<id>\d{1,5})/$',comment),
    url(r'^comment/(?P<pk>\d+)/$',restaurants.views.CommentView.as_view()),
    url(r'^math/$',session_test),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    #url(r'^index/$',views.IndexView.as_view()),
    url(r'^index/$',TemplateView.as_view(template_name='index1.html')),
    url(r'^accounts/register/$',register),
    url(r'^overview/$',overview),
    #url(r'^loaddata/$',loaddata),
    #url(r'^revisedata/$',revisedata),
    #url(r'^deletedata/$',deletedata),
    #url(r'^overview2/$',overview2),
    url(r'^plot/$',plotdata),
    url(r'^here/$',views.HereView.as_view()),
    url(r'^post/$',recv_data),
    url(r'^show/$',show),
    url(r'^load/$',load_data),
    url(r'^last/$',last),
    url(r'^findmachine/$',findmachine),
    url(r'^pr/$',pr),
]


