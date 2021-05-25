from django.shortcuts import render
from django.views import View


# Home app
class HomeView(View):
    def get(self, request,*args,**kwargs):
        hp = 'hey there guys'
        context ={
            'hp':hp
        }
        return render(request,'home/index.html', context)