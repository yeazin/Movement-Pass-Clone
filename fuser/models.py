from django.db import models
import uuid
from django.utils import tree
from sadmin.models import PassUser, District
# Qrcode Generator import 
import qrcode 
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Choices Fields 

class TimeSpend(models.Model):
    time = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.time

class MoveType(models.Model):
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.type 

class TakeCar(models.Model):
    name = models.CharField(max_length=20, null=True)

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
    user = models.ForeignKey(PassUser, on_delete=models.DO_NOTHING, null=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    from_m = models.CharField(max_length=200, blank=False, null=True, verbose_name='From Where')
    to_m = models.CharField(max_length=200, blank=False, null=True, verbose_name='To Where')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, verbose_name='District Name')
    sub_dristrict = models.CharField(max_length=200,verbose_name='Sub Dristrict Name', blank=True, null=True)
    time_spand = models.ForeignKey(TimeSpend, on_delete=models.CASCADE, null=True, default=None)
    move = models.ForeignKey(MoveType, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(auto_now_add=True)
    take_car = models.ForeignKey(TakeCar, on_delete=models.DO_NOTHING, null=True)
    car_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Car Number')
    reason = models.ForeignKey(MovementReason, on_delete=models.DO_NOTHING, null=True)
    qr_image = models.ImageField(upload_to='qr/',null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.reason } | {self.id}"

    def save(self,*args,**kwargs):
        img = qrcode.make(self.id)
        canvas = Image.new('RGB',(290, 290),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(img)
        frame = f"qr_code-{self.id}.png"
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_image.save(frame,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)





