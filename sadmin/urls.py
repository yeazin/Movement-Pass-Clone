from django.urls import path
from . import views

urlpatterns = [
    path('dasboard',views.Dashboard.as_view(), name='dashboard'),
    path('all/movement-pass/', views.AllPassView.as_view(), name='allpass'),
]