from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelStateFieldsCacheDescriptor
from fuser.models import District
import uuid

class IDtype(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Gender(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)

class PassUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=True, null=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField(null=True, auto_now_add=False)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, null=True)
    thana  = models.CharField(max_length=200, null=True, blank=True)
    id_name = models.ForeignKey(IDtype, on_delete=models.DO_NOTHING, verbose_name='Id Name Type')
    id_number = models.CharField(max_length=100, blank=False, null=True, verbose_name='Id Number')
    image = models.ImageField(upload_to = 'profile', null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.id } - { self.name }"


