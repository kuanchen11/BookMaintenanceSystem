from django.db import models
from accounts.models import Student

# Create your models here.
class BookCategory(models.Model):   # 書籍類別檔
    category_id = models.CharField(primary_key=True, max_length=10, null=False)  # 書籍類別id
    category_name = models.CharField(max_length=100, null=False)    # 書籍類別名稱

    def __str__(self):
        return self.category_name

class BookCode(models.Model):   # 書籍代碼檔
    code_id = models.CharField(primary_key=True, max_length=1, null=False)  # 書籍借閱狀態id(Y可以借出、N不可借出、B已借出)
    code_name = models.CharField(max_length=100, null=False)    # 書籍借閱狀態名稱

    def __str__(self):
        return self.code_name

class BookData(models.Model):   # 書籍資料檔
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, max_length=8, null=False)
    author = models.CharField(max_length=100, null=True)
    publisher = models.CharField(max_length=100, null=True)
    publish_date = models.DateField(max_length=40, null=True)
    summary = models.CharField(null=True, max_length=1000)
    price = models.IntegerField(null=True)
    keeper_id = models.IntegerField(null=True)
    status = models.ForeignKey(BookCode, on_delete=models.CASCADE, max_length=24, null=False)

    def __str__(self):
        return self.name

class BookLendRecord(models.Model):  # 書籍借閱紀錄檔
    book = models.ForeignKey(BookData, on_delete=models.CASCADE, null=False)
    borrower = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    borrow_date = models.DateField(null=False)

