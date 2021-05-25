from django.shortcuts import render,redirect
from .models import District, Subdistrict
from django.views import View
# models import 
from .models import District,Subdistrict,MovementReason,MovementPass
from sadmin.models import IDtype, Gender, PassUser
# essential imports
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Register for Movement Pass
class Register(View):
    def get(self,request,*args,**kwargs):
        gender_obj = Gender.objects.all()
        district_obj = District.objects.all().order_by('word')
        context={
            'gender':gender_obj,
            'district':district_obj
        }
        return render(request,'fuser/register.html',context)
    def post(self, request,*args,**kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        district_get = request.POST.get('district')
        district = District.objects.Get(name=district_get)
        gender_get = request.POST.get('gender')
        gender = Gender.objects.get(name=gender_get)
        dob = request.POST.get('date')
        thana = request.POST.get('thana')
        id_name_get = request.POST.get('id_name')
        id_name = IDtype.objects.get(name=id_name_get)
        image = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number_check = User.objects.filter(username=phone)
        if phone_number_check:
            messages.warning(request,'Phone Number Already Exits !!!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        elif password1 != password2 :
            messages.warning(request,'Password didnot Match !!!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else :
            auth_info={
                'username':phone,
                'password':make_password(password1)
            }
            user = User(**auth_info)
            user.save()
        user_obj = PassUser(user=user,name=name, gender=gender,district=district,\
                    thana=thana,image=image,)
        
        


# Login For  Movement Pass
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'fuser/login.html')

# Dashboard for Movement Pass
class Dashboard(View):
    def get(self,request,*args,**kwargs):
        return render(request,'fuser/dashboard.html')

# Apply for Movement Pass
class ApplyPass(View):
    def get(self,request,*args,**kwargs):
        district_obj = District.objects.all()
        move_reason_obj = MovementReason.objects.all()
        move = MovementPass.objects.all()
        context ={
            'district':district_obj,
            'move':move_reason_obj,
            'obj':move
        }
        return render(request,'fuser/pass_apply.html', context)

    def post(self,request,*args,**kwargs):
        _from = request.POST.get('from')
        _to = request.POST.get('to')
        district_obj = request.POST.get('district')
        district = District.objects.get(district=district_obj)
        subdistrict = request.POST.get('subdistrict')
        reason_obj = request.POST.get('reason')
        reason = MovementReason.objects.get(reason=reason_obj)

        movementpass_obj = MovementPass(_from=_from,_to=_to,
                                    district=district,
                                    sub_dristrict=sub_dristrict,
                                    reason=reason)
        movementpass_obj.save()
        return redirect('home')
        





