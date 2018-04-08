from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse

# Create your models here.

class User(models.Model):
    gender = (
        ('male',"男"),
        ('female',"女")
        )
 
    #数据库中字段是否可以建立唯一索引(unique=True)
    #auto_now_add        创建时自动更新当前时间
    name = models.CharField(max_length=128,unique=True) 
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.name +":"+ self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
            
        