from django.contrib import admin
from . import models

# Register your models here.
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')  # 在列表中顯示的欄位
    ordering = ('category_id',)

admin.site.register(models.BookCategory, BookCategoryAdmin)

class BookCodeAdmin(admin.ModelAdmin):
    list_display = ('code_id', 'code_name')  # 在列表中顯示的欄位

admin.site.register(models.BookCode, BookCodeAdmin)

class BookDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'author', 'publisher', 'publish_date', 'price', 'keeper_id', 'status')  # 在列表中顯示的欄位
    ordering = ('id',)

admin.site.register(models.BookData, BookDataAdmin)

class BookLendRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'borrower', 'borrow_date')  # 在列表中顯示的欄位
    ordering = ('id',)

admin.site.register(models.BookLendRecord, BookLendRecordAdmin)