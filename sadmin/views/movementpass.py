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

# All Pass view
class AllPassView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        pass_obj = MovementPass.objects.all()
        context={
            'pass':pass_obj
        }
        return render (request,'sadmin/pass/all_pass.html',context)


# single View of Movement Pass
class SinglePass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,id):
        pass_obj = get_object_or_404(MovementPass,id=id)
        context= {
            'obj':pass_obj
        }
        return render(request,'sadmin/pass/pass_single.html',context)

# Approved pass Views
class ViewApprovedPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        approve_pass_obj = MovementPass.objects.filter(is_approved= True)
        context = {
            'approved_pass':approve_pass_obj
        }
        return render(request,'sadmin/pass/approved_pass.html',context)

# Disapproved pass Views
class ViewDisapprovedPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        disapprove_pass_obj = MovementPass.objects.filter(is_approved= False)
        context = {
            'disapproved_pass':disapprove_pass_obj
        }
        return render(request,'sadmin/pass/disapproved_pass.html',context)

# Exprired Pass Views
class ViewExpiredPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        expired_pass_obj = MovementPass.objects.filter(is_expired = True)
        context = {
            'expired_pass':expired_pass_obj
        }
        return render(request,'sadmin/pass/expired_pass.html',context)