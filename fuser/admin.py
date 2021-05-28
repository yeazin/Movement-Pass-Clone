from django.contrib import admin
from .models import District, MovementReason, \
    MovementPass, MoveType, TakeCar,TimeSpend
# Register your models here.

admin.site.register(District)
#admin.site.register(Subdistrict)
admin.site.register(MovementReason)
admin.site.register(MovementPass)
admin.site.register(TimeSpend)
admin.site.register(MoveType)
admin.site.register(TakeCar)