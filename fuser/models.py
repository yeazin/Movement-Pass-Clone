from django.db import models
import uuid
from django.utils import tree
from sadmin.models import PassUser, District



# Choices Fields 

spend = (
    ('1', 'One Hour'),
    ('2', 'Two Hour'),
    ('3', 'Three Hour'),
    ('4', 'Four Hour'),
    ('5', 'Six Hour'),
    ('6', ' Eight Hour')
)

move_type =(
    ('1', 'Come and Go'),
    ('2', 'Only Go'))

drive = (
    ('1', 'Yes'),
    ('2',' No')   
)

take_car = (
    ('1', 'Yes'),
    ('2','No')
)


# Subdistrict
class Subdistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, verbose_name='District Name')
    sub_name = models.CharField(max_length=100, verbose_name='Sub District Name' , blank=False, null=True)

    def __str__(self):
        return self.sub_name

class MovementReason(models.Model):
    reason = models.CharField(max_length=200,blank=False, null=True)

    def __str__(self):
        return self.reason

# Movement Pass Model
class MovementPass(models.Model):
    user = models.ForeignKey(PassUser, on_delete=models.DO_NOTHING, null=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    _from = models.CharField(max_length=200, blank=False, null=True, verbose_name='From Where')
    _to = models.CharField(max_length=200, blank=False, null=True, verbose_name='To Where')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, verbose_name='District Name')
    sub_dristrict = models.CharField(max_length=200,verbose_name='Sub Dristrict Name', blank=True, null=True)
    time_spand = models.CharField(max_length=20, choices=spend, verbose_name='Time spending')
    move = models.CharField(max_length=20, choices=move_type, default='1', verbose_name='Movement Type')
    date = models.DateTimeField(auto_now_add=True)
    take_car = models.CharField(max_length=3,choices=take_car,null=True, default='2')
    car_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Car Number')
    drive = models.CharField(max_length=10, choices=drive, default='2', verbose_name='Drive Your self ?')
    reason = models.ForeignKey(MovementReason, on_delete=models.DO_NOTHING, null=True)
    is_approved = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.reason } | {self.id}"





