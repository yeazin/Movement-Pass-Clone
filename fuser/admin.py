from django.contrib import admin
from .models import District, MovementReason, \
    MovementPass, MoveType,TimeSpend



admin.site.register(District)
#admin.site.register(Subdistrict)
admin.site.register(MovementReason)
admin.site.register(MovementPass)
admin.site.register(TimeSpend)
admin.site.register(MoveType)
