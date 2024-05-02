from django.contrib import admin
from . import models

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'studentId', 'register_year', 'email', 'phone_number', 'gender', 'birth_date')  # 在列表中顯示的欄位
    ordering = ('id',)

admin.site.register(models.Student, StudentAdmin)