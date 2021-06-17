from django.urls import path
from . import views
from .views.user_view import Register, EditProfile,\
                            LogoutView,LoginView
from .views.pass_view import Dashboard,PassApply,\
                            CollectPass,ViewPass

urlpatterns = [
    path('movement-pass/apply/', PassApply.as_view(), name="apply"),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
     
    path('edit/profile/', EditProfile.as_view(), name='edit_profile'),
    
    path('movement-pass/collect/',CollectPass.as_view(), name='collect'),
    path('movement-pass/view/<str:id>/',ViewPass.as_view(), name='single'),
]