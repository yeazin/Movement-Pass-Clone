
from django.contrib import admin
from django.urls import path , include
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('sadmin/', admin.site.urls),
    path('',views.HomeView.as_view(), name='home'),
    # app url
    path('user/', include('fuser.urls')),
    path('admin/', include('sadmin.urls'))
]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
