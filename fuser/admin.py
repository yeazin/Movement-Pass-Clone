from django.contrib import admin
from .models import District, Subdistrict, MovementReason, MovementPass
# Register your models here.

admin.site.register(District)
admin.site.register(Subdistrict)
admin.site.register(MovementReason)
admin.site.register(MovementPass)