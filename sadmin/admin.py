from django.contrib import admin
from .models import IDtype, PassUser, Gender

# Register your models here.

admin.site.register(IDtype)
admin.site.register(PassUser)
admin.site.register(Gender)