from django.shortcuts import get_object_or_404, redirect, render
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
from django.contrib import messages


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

# Approved pass Views
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

### Condition Vews
# approve views
class MakeApprove(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        obj = get_object_or_404(MovementPass,id=id)
        obj.is_approved == True
        obj.save()
        messages.success(request,'{obj.id} has been approved!!')
        return redirect ('allpass')

# Disapprove views 
class MakeDisapprove(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        obj = get_object_or_404(MovementPass,id=id)
        obj.is_approved == False
        obj.save()
        messages.success(request,'{obj.id} has been Disapproved!!')
        return redirect ('allpass')

# Exprires Views
class MakeExpire(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        obj = get_object_or_404(MovementPass,id=id)
        obj.is_expired == True
        obj.save()
        messages.success(request,'{obj.id} has been Expired!!')
        return redirect ('allpass')

# Delete Views
class DeletePass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,id):
        obj = get_object_or_404(MovementPass,id=id)
        obj.delete()
        messages.warning(request,'{obj.id} has been Deleted!!')
        return redirect ('allpass')

# Movement Reason 
class MovementReasonView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        reason_obj = MovementReason.objects.all().order_by('-id')
        context ={
            'reason':reason_obj
        }
        return render (request,'sadmin/reason/reason.html', context)
    def post(self,request):
        reason = request.POST.get('reason')
        reason_get = MovementReason(reason=reason)
        reason_get.save(reason_get)
        messages.success(request,'New Movement Reason has been added')
        return redirect('reason')

# Delete Movement Reason 
class DeleteMovementReasonView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request,id):
        reason_obj = get_object_or_404(MovementReason,id=id)
        reason_obj.delete()
        messages.warning(request, ' The reason has been deleted')
        return redirect('reason')

# District Views
class DistrictView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        district_obj = District.objects.all().order_by('name')
        context ={
            'district':district_obj
        }
        return render(request,'sadmin/district/district.html',context)
    
    def post(self,request):
        distict_obj = request.POST.get('district')
        district = District(name=distict_obj)
        district.save(distict_obj)
        messages.success(request,'District Has Been Added')
        return redirect('district')

# Delete District 
class DeleteDistrict(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self, request,id):
        district_obj = get_object_or_404(District, id=id)
        district_obj.delete()
        messages.warning(request,'The District has been deleted')
        return redirect('district')

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