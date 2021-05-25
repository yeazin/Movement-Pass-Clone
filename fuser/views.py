from django.shortcuts import render,redirect
from .models import District, Subdistrict
from django.views import View
from .models import District,Subdistrict,MovementReason,MovementPass


# Register for Movement Pass
class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,'fuser/register.html')

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
        





