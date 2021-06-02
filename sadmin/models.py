from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date, datetime


class IDtype(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Gender(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)

# address type
class District(models.Model):
    name = models.CharField(max_length=100,verbose_name='District name', blank=False, null=True)

    def __str__(self):
        return self.name

class PassUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=300, blank=True, null=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField(null=True, auto_now_add=False)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, null=True)
    thana  = models.CharField(max_length=200, null=True, blank=True)
    id_name = models.ForeignKey(IDtype, on_delete=models.DO_NOTHING, verbose_name='Id Name Type')
    id_number = models.CharField(max_length=100, blank=False, null=True, verbose_name='Id Number')
    created_at = models.DateField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to = 'profile', null=True)
    is_admin = models.BooleanField(default=False)
    '''
    def age(self):
        today = datetime.date.today()
        age_finder = today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        return age_finder
    '''
    def calculateAge(self):
        today = date.today()
        age = today.year - self.year - ((today.month, today.day) <(self.month, self.day))
  
        return age

    def __str__(self):
        return f"{ self.id } - { self.name }"


