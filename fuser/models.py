from django.db import models
import uuid


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

# address type
class District(models.Model):
    name = models.CharField(max_length=100,verbose_name='District name', blank=False, null=True)

    def __str__(self):
        return self.name

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
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    _from = models.CharField(max_length=200, blank=False, null=True, verbose_name='From Where')
    _to = models.CharField(max_length=200, blank=False, null=True, verbose_name='To Where')
    traking_id = models.IntegerField(null=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, verbose_name='District Name')
    sub_dristrict = models.CharField(max_length=200,verbose_name='Sub Dristrict Name', blank=True, null=True)
    time_spand = models.CharField(max_length=20, choices=spend, default='1', verbose_name='Time spending')
    move = models.CharField(max_length=20, choices=move_type, default='1', verbose_name='Movement Type')
    date = models.DateTimeField(auto_now_add=True)
    take_car = models.BooleanField(default=False)
    car_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Car Number')
    drive = models.CharField(max_length=10, choices=drive, default='2', verbose_name='Drive Your self ?')
    reason = models.ForeignKey(MovementReason, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.reason)





