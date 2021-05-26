from django.urls import path
from . import views

urlpatterns = [
    path('apply/pass/', views.ApplyPass.as_view(), name='apply'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/',views.Dashboard.as_view(), name='dashboard'),
]