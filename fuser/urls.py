from django.urls import path
from . import views
from .views1.user_view import Register, EditProfile,\
                            LogoutView,LoginView

urlpatterns = [
    path('movement-pass/apply/', views.PassApply.as_view(), name="apply"),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
     
    path('edit/profile/', EditProfile.as_view(), name='edit_profile'),
    
    path('movement-pass/collect/',views.CollectPass.as_view(), name='collect'),
    path('movement-pass/view/<str:id>/', views.ViewPass.as_view(), name='single'),
]