from django.db import models

# Create your models here.

#User model
class User(models.Model):
    username = models.CharField(max_length=100,default='null')
    password = models.CharField(max_length=100,default='null')
    name = models.CharField(max_length=100,default='null')
    status = models.IntegerField(default=0)
    department_id = models.CharField(max_length=11,default='null')
    desc = models.CharField(max_length=255,default='null')
    register_date = models.DateField(auto_now_add=True)
    last_login_date = models.DateField(auto_now=True)

#User permission model
#class Permission(models.Model):



#Role model
#class Role(models.Model):
