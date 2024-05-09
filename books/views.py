from django.shortcuts import render
from .models import BookCategory, BookData, BookLendRecord, BookCode
from .forms import BookSearchForm
from accounts.models import Student
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def book(request):
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    books = BookData.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        book_name = request.POST.get('book-title')
        category_id = request.POST.get('category_id')
        borrower_id = request.POST.get('borrower_id')
        book_status = request.POST.get('book_status')
        form = BookSearchForm(request.POST)
        # 構建查詢條件
        conditions = Q()
        if book_name:
            conditions &= Q(name__contains=book_name)
        if category_id:
            conditions &= Q(category_id=category_id)
        if borrower_id:
            conditions &= Q(keeper_id=borrower_id)
        if book_status:
            conditions &= Q(status_id=book_status)
        
        
        books = books.filter(conditions)
        
        
        if form.is_valid():
            # 在此處理表單提交
            pass
    else:
        form = BookSearchForm()
    return render(request, 'books/book.html', locals())

