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
        total_expired_pass = pass_obj.filter(is_expired = True ).count()
        total_district = District.objects.all().count()
        total_time = TimeSpend.objects.all().count()
        total_reason = MovementReason.objects.all().count()
        recent_users = PassUser.objects.all().order_by('-created_at')[:5]
        recent_pass = MovementPass.objects.all().order_by('-id')[:5]
        context = {
            'total_user':total_user,
            'total_pass':total_pass,
            'approved':total_approved_pass,
            'pending':total_pending_pass,
            'total_expired':total_expired_pass,
            'total_reason':total_reason,
            'district':total_district,
            'time':total_time,
            'recent_users':recent_users,
            'recent_pass':recent_pass
        }
        return render (request,'sadmin/home/admin_dashboard.html',context)

# Search Function 
class SearchAdmin(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        search = request.GET['q']
        pass_obj = MovementPass.objects.all()
        if len(search) > 100:
            pass_obj_check = pass_obj.none()
        else:
            pass_obj_check = pass_obj.filter(
                Q(user__name__icontains= search) |
                Q(id__icontains= search)|
                Q(from_m__icontains=search)|
                Q(to_m__icontains=search)|
                Q(district__name__icontains=search)|
                Q(sub_dristrict__icontains=search)|
                Q(time_spand__time__icontains=search)|
                Q(move__name__icontains=search)|
                Q(date__icontains=search)|
                Q(reason__reason__icontains=search)
            )
        context ={
            'search':search,
            'pass':pass_obj_check
        }
        return render(request,'sadmin/home/search.html', context)