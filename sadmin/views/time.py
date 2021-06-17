from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
# models import 
from fuser.models import *
from sadmin.models import *
# essential imports
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.contrib import messages
from django.db.models import Q

# Time spends Views
class TimeSpendsView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        time_obj = TimeSpend.objects.all()
        context ={
            'time':time_obj
        }
        return render(request,'sadmin/time/time.html', context)
        
    def post(self, request):
        time_get = request.POST.get('time')
        time = TimeSpend(time=time_get)
        time.save(time_get)
        messages.success(request,'Time Hours Has Been Added')
        return redirect('time')

# Delete time Spends
class DeleteTime(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request,id):
        time_get= get_object_or_404(TimeSpend,id=id)
        time_get.delete()
        messages.warning(request,'Time Hour has been deleted')
        return redirect('time')