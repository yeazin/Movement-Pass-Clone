from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
# models import 
from .models import MovementReason,MovementPass, TimeSpend,\
    MoveType, TakeCar 
from sadmin.models import IDtype, Gender, PassUser,District
# essential imports
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Register for Movement Pass
class Register(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        gender_obj = Gender.objects.all()
        district_obj = District.objects.all().order_by('name')
        id_obj = IDtype.objects.all()
        context={
            'gender':gender_obj,
            'id_':id_obj,
            'district':district_obj
        }
        return render(request,'fuser/register.html',context)
    def post(self, request,*args,**kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        district_get = request.POST.get('district')
        district = District.objects.get(name=district_get)
        gender_get = request.POST.get('gender')
        gender = Gender.objects.get(name=gender_get)
        dob = request.POST.get('date')
        thana = request.POST.get('thana')
        id_name_get = request.POST.get('id_name')
        id_name = IDtype.objects.get(name=id_name_get)
        id_number = request.POST.get('id_number')
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
                    thana=thana,image=image,id_number=id_number,\
                    id_name=id_name,date_of_birth = dob)
        user_obj.save()
        messages.success(request,'Please Login to Continue')
        return redirect('login')


# Edit Profile 
class EditProfile(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    def get(self,request):
        gender_obj = Gender.objects.all()
        district_obj = District.objects.all().order_by('name')
        id_obj = IDtype.objects.all()
        context={
            'gender':gender_obj,
            'id_':id_obj,
            'district':district_obj
        }
        return render(request,'fuser/profile_edit.html', context )

    def post(self,request):
        obj = request.user.passuser
        #id_obj = request.POST.get('id_type')
        #obj.id_name = IDtype.objects.get(name=id_obj)
        gender_obj = request.POST.get('gender')
        obj.gender = Gender.objects.get(name=gender_obj)
        district_obj = request.POST.get('district')
        obj.district = District.objects.get(name=district_obj)
        obj.thana = request.POST.get('thana') 
        obj.id_number = request.POST.get('id_number')
        img = obj.image = request.FILES.get('image')
        if not img:
            pass 
        
        obj.save()
        messages.success(request,'Profile has been Updated')
        return redirect ('home')
        


# Login For  Movement Pass
class LoginView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request,'fuser/login.html')
    def post(self,request,*args,**kwargs):
        uname = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
            '''
            check = user.passuser_set.filter(is_admin=True)
            if check :
                login(request, user)
                return redirect('home')
            elif not check:
                login(request, user)
                return redirect('dashboard')
            '''
        else:
            messages.warning(request,'Phone Number or Password Didnot Match')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Logout View
class LogoutView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')

# Dashboard for Movement Pass
class Dashboard(View):
    def get(self,request,*args,**kwargs):
        return render(request,'fuser/dashboard.html')

# Apply for Movement Pass
class ApplyPass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    def get(self,request):
         
        district_obj = District.objects.all().order_by('name')
        reason_obj = MovementReason.objects.all().order_by('reason')
        spend_obj  = TimeSpend.objects.all()
        car_obj = TakeCar.objects.all()
        move_obj = MoveType.objects.all()
        context ={
            'district':district_obj,
            'reason':reason_obj,
            'spend':spend_obj,
            'car':car_obj,
            'move':move_obj
        }
        return render(request,'fuser/pass_apply.html', context)

    def post(self,request):
        user = request.user.passuser 
        from_m = request.POST.get('from')
        to_m = request.POST.get('to')
        #district_get = request.POST.get('district')
        #district = District.objects.get(name=district_get)
        subdistrict = request.POST.get('subdistrict')
        date = request.POST.get('date')
        #time_spand_obj = request.POST.get('district')
        #time_spand = TimeSpend.objects.get(time=time_spand_obj)
        #move_get = request.POST.get('move')
        #move = MoveType.objects.get(type=move_get)
        #reason_get = request.POST.get('reason')
        #reason = MovementReason.objects.get(reason=reason_get)
        movement_obj = MovementPass(user=user,from_m=from_m,to_m=to_m,\
                #district=district,
                #subdistrict=subdistrict,\
                date=date,#move=move,reason=reason,
                #time_spand=time_spand
                )
        movement_obj.save()
        return redirect('collect')

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

        





