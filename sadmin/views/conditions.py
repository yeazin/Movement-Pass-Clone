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


# approve views
class MakeApprove(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        obj = MovementPass.objects.get(id=id)
        obj.is_approved == True
        obj.save()
        messages.success(request,'Pass has been approved!!')
        # Redirect To the Same Page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Disapprove views 
class MakeDisapprove(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        obj = MovementPass.objects.get(id=id)
        obj.is_approved == False
        obj.save()
        messages.success(request,'Pass has been Disapproved!!')
         # Redirect To the Same Page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Exprires Views
class MakeExpire(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        obj = MovementPass.objects.get(id=id)
        obj.is_expired == True
        obj.save()
        messages.success(request,'Pass has been Expired!!')
        # Redirect To the Same Page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Delete Views
class DeletePass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,id):
        obj = get_object_or_404(MovementPass,id=id)
        obj.delete()
        messages.warning(request,'The pass has been Deleted!!')
        return redirect ('allpass')