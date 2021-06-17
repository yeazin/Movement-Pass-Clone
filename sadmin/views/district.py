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