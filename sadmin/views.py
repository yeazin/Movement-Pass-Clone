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

### Condition Vews
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



