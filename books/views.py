from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from .models import BookCategory, BookData, BookLendRecord, BookCode
from .forms import BookSearchForm
from accounts.models import Student
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

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

@csrf_exempt
@login_required(login_url='/login/')
def book_delete(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    # 如果書籍狀態是借出中，則無法刪除
    if book.status.code_id == 'B':
        return JsonResponse({'message': 'unable'})
    else:
        book.delete()
        return JsonResponse({'message': 'success'})


@login_required(login_url='/login/')
def book_create(request):
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
  
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        category_id = request.POST.get("category_id")
        author = request.POST.get("book_author")
        publisher = request.POST.get("publisher")
        publish_date = request.POST.get("publish_date")
        summary = request.POST.get("summary")
        price = request.POST.get("price")
        borrower_id = request.POST.get("borrower_id")
        book_status = request.POST.get("book_status")

        if price == '':
            price = None
        else:
            price = int(price)
            
        if publish_date == '':
            publish_date = None
            
        category = BookCategory.objects.get(category_id=category_id)
        status = BookCode.objects.get(code_id=book_status)
        book = BookData(name=book_name, category=category, author=author, publisher=publisher, publish_date=publish_date, summary=summary, price=price, keeper_id=borrower_id, status=status)
        book.save()
        
        if borrower_id:
            borrower = Student.objects.get(id=borrower_id)
            lendrec = BookLendRecord(book=book, borrow=borrower, borrow_date=datetime.now().date())
            lendrec.save()
        return redirect(reverse('Book'))
    
    return render(request, 'books/bookcreate.html', locals())


@login_required(login_url='/login/')
def book_edit(request):
    return render(request, 'books/bookedit.html', locals())


@login_required(login_url='/login/')
def book_details(request):
    return render(request, 'books/details.html', locals())


@login_required(login_url='/login/')
def book_lendrec(request):
    return render(request, 'books/booklendrec.html', locals())