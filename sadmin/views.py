from django.shortcuts import render
from django.views.generic import View
# models import 
from fuser.models import *
from .models import *
# essential imports
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Count


class Dashboard(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        total_user = PassUser.objects.all().count()
        pass_obj = MovementPass.objects.all()
        total_pass = pass_obj.count()
        total_approved_pass = pass_obj.filter(is_approved=True).count()
        total_pending_pass = pass_obj.filter(is_approved=False).count()
        context = {
            'total_user':total_user,
            'total_pass':total_pass,
            'approved':total_approved_pass,
            'pending':total_pending_pass
        }
        return render (request,'sadmin/home/admin_dashboard.html',context)
    