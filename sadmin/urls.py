from django.urls import path
# views import 
from .views.dashboard import Dashboard,SearchAdmin
from .views.conditions import MakeApprove,MakeDisapprove,\
                                MakeExpire,DeletePass
from .views.users import AllUsers, SingleUser 
from .views.movementpass import AllPassView,SinglePass,ViewApprovedPass,ViewDisapprovedPass,ViewExpiredPass
from .views.district import DeleteDistrict, DistrictView
from .views.time import TimeSpendsView,DeleteTime
from .views.reasons import MovementReason, DeleteMovementReasonView, MovementReasonView

urlpatterns = [
    path('dasboard',Dashboard.as_view(), name='dashboard'),
    path('movement-pass/all/search/query/',SearchAdmin.as_view(), name='search'),

    path('all/movement-pass/',AllPassView.as_view(), name='allpass'),
    path('view/movement-pass/<str:id>/', SinglePass.as_view(), name='single_pass'),

    path('movement-pass/view/all/approved',ViewApprovedPass.as_view(),name='approved_pass'),
    path('movement-pass/view/all/disapproved',ViewDisapprovedPass.as_view(),name='disapproved_pass'),
    path('movement-pass/view/all/expired',ViewExpiredPass.as_view(),name='expired_pass'),

    path('view/all-users/movementpass/', AllUsers.as_view(),name='all_users'),
    path('movement-pass/view/user/<str:id>',SingleUser.as_view(), name='single_user'),
    
    path('movement-pass/<str:id>/approved/', MakeApprove.as_view(), name='approved'),
    path('movement-pass/<str:id>/disapproved/',MakeDisapprove.as_view(), name='disapproved'),
    path('movement-pass/<str:id>/expired/',MakeExpire.as_view(), name='expired'),
    path('movement-pass/<str:id>/Delete/', DeletePass.as_view(), name='deleted'),

    path('movement-pass/view/movement-reasons/',MovementReasonView.as_view() ,name='reason'),
    path('movement-pass/view/movement-reasons/delete/<str:id>/', DeleteMovementReasonView.as_view(), name='delete_reason'),

    path('movement-pass/view/district/', DistrictView.as_view(), name='district'),
    path('movement-pass/delete/district/<str:id>',DeleteDistrict.as_view(),name='delete_district'),

    path('movement-pass/view/time-hours/', TimeSpendsView.as_view(), name='time'),
    path('movement-pass/delete/time-hours/<str:id>', DeleteTime.as_view(), name='delete_time'),
]