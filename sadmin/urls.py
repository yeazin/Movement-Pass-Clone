from django.urls import path
from . import views

urlpatterns = [
    path('dasboard',views.Dashboard.as_view(), name='dashboard'),
    path('all/movement-pass/', views.AllPassView.as_view(), name='allpass'),
    path('view/movement-pass/<str:id>/', views.SinglePass.as_view(), name='single_pass'),
    path('view/all-users/movementpass/', views.AllUsers.as_view(),name='all_users'),
    path('movement-pass/view/user/<str:id>',views.SingleUser.as_view(), name='single_user'),
]