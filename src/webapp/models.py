from typing import Optional
from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager, Group, Permission
from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

from .decorator import unauthenticated_user




class User(AbstractUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INF = "INF", "Informatica"
        ELE = "ELE", "Electrica"
        MEC = "MEC", "Mecanica"

    base_role = Role.ADMIN
    USERNAME_FIELD = "username"


    role = models.CharField(max_length=50, choices=Role.choices)
    
    

    
        


    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

AUTH_USER_MODEL = "webapp.User"





class infManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INF)


class inf(User):
    base_role = User.Role.INF

    infor = infManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Informatica"



@receiver(post_save, sender=inf)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'INF':
        InfProfile.objects.create(user=instance)


class InfProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inf_id = models.IntegerField(null=True, blank=True) 






class eleManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ELE)


class ele(User):
    base_role = User.Role.ELE

    elect = eleManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Electrica"

@receiver(post_save, sender=ele)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'ELE':
        EleProfile.objects.create(user=instance)

class EleProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ele_id = models.IntegerField(null=True, blank=True)








class mecManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MEC)


class mec(User):
    base_role = User.Role.MEC

    mecan = mecManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Mecanica"

@receiver(post_save, sender=mec)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'MEC':
        MecProfile.objects.create(user=instance)

class MecProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mec_id = models.IntegerField(null=True, blank=True)




class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    detalle = models.CharField(max_length=2000)
    detalle_corto = models.CharField(max_length=100)
    TIPO_CHOICES = [
        ("S", "Suspención de actividades"),
        ("C", "Suspención de clase"),
        ("I", "Información")
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default="I")
    ROLES_CHOICES = [
        ("ADMIN", "Admin"),
        ("INF", "Informatica"),
        ("ELE", "Electrica"),
        ("MEC", "Mecanica")
    ]
    ROLE = models.CharField(max_length=5, choices=ROLES_CHOICES, default="ADMIN")
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True) 