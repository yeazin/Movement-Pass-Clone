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