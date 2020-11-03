from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
from quiz.models import *

class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)
    contact = models.CharField(unique=True, max_length=12)
    password = models.CharField(max_length=200)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    step1 = models.SmallIntegerField()
    step2 = models.SmallIntegerField()
    step3 = models.SmallIntegerField()
    step4 = models.SmallIntegerField()


    class Meta:
        managed = True
        db_table = 'user'
