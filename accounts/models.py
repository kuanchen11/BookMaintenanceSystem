from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):    # 學生資料檔
    studentId = models.CharField(max_length=10, unique=True, null=True)  # 學號，必須唯一
    register_year = models.IntegerField(null=True)  # 註冊年
    phone_number = models.CharField(max_length=10, null=True)  # 手機號碼
    gender = models.CharField(max_length=1, null=True)  # 性別，M: 男性，F: 女性
    birth_date = models.DateField(null=True)  # 生日
