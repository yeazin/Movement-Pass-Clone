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

# All users 
class AllUsers(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        all_users = PassUser.objects.all().order_by('-created_at')
        
        context ={
            'all_users':all_users,
            
        }
        return render (request,'sadmin/pass/users.html', context)

# Single User view
class SingleUser(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,id):
        user_obj = get_object_or_404(PassUser,id=id)
        user_pass_obj  = user_obj.movementpass_set.all().order_by('-id')
        context={
            'user':user_obj,
            'user_pass':user_pass_obj
        }
        return render(request,'sadmin/pass/single_user.html',context)
