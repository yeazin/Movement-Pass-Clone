from django.db import models
from django.contrib.auth.models import User
from fuser.models import District
import uuid

class IDtype(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class PassUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, null=True)
    thana  = models.CharField(max_length=200, null=True, blank=True)
    idnumber = models.ForeignKey(IDtype, on_delete=models.DO_NOTHING)
    id_name = models.CharField(max_length=100, blank=False, null=True)
    image = models.ImageField(upload_to = 'profile', null=True)

    def __str__(self):
        return f"{ self.id } - { self.name }"


