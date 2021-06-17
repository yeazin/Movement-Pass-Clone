from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
# models import 
from fuser.models import MovementReason,MovementPass, TimeSpend,\
    MoveType
from sadmin.models import IDtype, Gender, PassUser,District
# essential imports
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# forms import 
from fuser.forms import PassApplyForm


# Dashboard for Movement Pass
class Dashboard(View):
    def get(self,request,*args,**kwargs):
        return render(request,'fuser/dashboard.html')


# Apply for Movement Pass
class PassApply(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        forms = PassApplyForm()
        context = {
            'forms':forms 
        }  
        return render(request, 'fuser/pass_apply.html', context)    
    def post(self,request):
        forms = PassApplyForm(request.POST)
        if forms.is_valid:
            obj = forms.save(commit=False)
            # current user requirment 
            obj.user = request.user.passuser 
            obj.save()
            return redirect('collect')
        else:
            messages.warning(request,'Please Fill Up the Form Again')
            return redirect('apply')
# Collect Pass View
class CollectPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        user = request.user
        pass_obj = user.passuser.movementpass_set.all().order_by('-id')
        context ={
            'pass':pass_obj,
            'user':user
        }
        return render(request,'fuser/collect.html',context)

# View pass 
class ViewPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,id):
        obj = get_object_or_404(MovementPass,id=id)
        context ={
            'obj':obj
        }
        return render(request,'fuser/single_pass.html',context)

