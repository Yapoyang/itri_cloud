from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.template import RequestContext
from restaurants.models import Restaurant, Food, Comment
from restaurants.forms import CommentForm
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from django.contrib import auth
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
# Create your views here.

def menu(request,id):
    if id:
        restaurant=Restaurant.objects.get(id=id)
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")    

class MenuView(DetailView):
      model=Restaurant
      template_name='menu.html'
      context_object_name='restaurant'


@login_required
def list_restaurants(request):
    restaurants=Restaurant.objects.all()
    #print(request.user.user_permissions.all())
    request.session['restaurants']=restaurants
    return render_to_response('restaurants_list.html',locals(),RequestContext(request))

class RestaurantsView(ListView):
      model=Restaurant
      template_name='restaurants_list.html'
      context_object_name='restaurants'

def user_can_comment(user):
    return user.is_authenticated and user.has_perm('restaurants.can_comment')

@permission_required('restaurants.can_comment',login_url='/accounts/login/')
def comment(request,id):
    if id:
        r=Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if request.POST:
        f=CommentForm(request.POST)
        if f.is_valid():
            visitor=f.cleaned_data['visitor']
            content=f.cleaned_data['content']
            email=f.cleaned_data['email']
            date_time=timezone.localtime(timezone.now())
            c=Comment.objects.create(visitor=visitor,
		    email=email,
		    content=content,
		    date_time=date_time,
		    restaurant=r)
            f=CommentForm(initial={'content':'No comment'})
    else:
        f=CommentForm(initial={'content':'No comment'})
    return render_to_response('comments.html',locals())
#path=request.path
    #restaurants=Restaurant.objects.get(id=1)
    #return render_to_response('menu.html',locals())

class CommentView(FormView,SingleObjectMixin):
      form_class=CommentForm
      template_name='comments.html'
      success_url='/comment/'
      initial={'content':'Write here if u have comment'}
      model=Restaurant
      context_object_name='r'
     
      def form_valid(self,form):
          c=Comment.objects.create(
              visitor=form.cleaned_data['visitor'],
              email=form.cleaned_data['email'],
              content=form.cleaned_data['content'],
              date_time=timezone.localtime(timezone.now()),
              restaurant=self.get_object()
          )
          return self.render_to_response(self.get_context_data(form=self.form_class(initial=self.initial)))
      def get_context_data(self,**kwargs):
          self.object=self.get_object()
          return super(CommentView, self).get_context_data(object=self.object,**kwargs)
  
@login_required
def list_users(request):
    users=auth.models.User.objects.all()
    return render_to_response('user_list.html',locals())

@login_required
def list(request,model):
    objs=model.objects.all()
    return render_to_response('{0}s_list.html'.format(model.__name__.lower()),locals())



