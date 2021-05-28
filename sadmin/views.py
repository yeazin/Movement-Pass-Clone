from django.shortcuts import render
from django.views.generic import View
# models import 
#from fuser.models import MovementReason,MovementPass
from .models import IDtype, Gender, PassUser, District
# essential imports
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Dashboard(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        return render (request,'sadmin/admin_dashboard.html')
    