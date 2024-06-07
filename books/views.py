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
        form = BookSearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data.get('book_title')
            category_id = form.cleaned_data.get('category_id')
            borrower_id = form.cleaned_data.get('borrower_id')
            book_status = form.cleaned_data.get('book_status')
            conditions = Q()
            if book_name:
                conditions &= Q(name__icontains=book_name)
            if category_id:
                conditions &= Q(category_id=category_id)
            if borrower_id:
                conditions &= Q(keeper_id=borrower_id.id)
            if book_status:
                conditions &= Q(status_id=book_status)
            
            books = books.filter(conditions)
    else:
        form = BookSearchForm()

    return render(request, 'books/book.html', locals())


@csrf_exempt
@login_required(login_url='/login/')
def book_delete(request, book_id):
    if request.method == 'DELETE':
        book = get_object_or_404(BookData, id=book_id)
        if book.status.code_id == 'B':
            return JsonResponse({'message': 'unable'})
        else:
            book.delete()
            return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)


@login_required(login_url='/login/')
def book_create(request):
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    today = datetime.today()
  
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

        if not price:
            price = None
        else:
            price = int(price)
            
        if not publish_date:
            publish_date = None
            
        if not borrower_id:
            borrower_id = None

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
def book_edit(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    today = datetime.today()

    if book.keeper_id:
        keeper = get_object_or_404(Student, id=book.keeper_id)
        keeper_name = keeper.username
        
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
        
        if not price:
            price = None
        else:
            price = int(price)
            
        if not publish_date:
            publish_date = None
        
        if not borrower_id:
            borrower_id = None
            
        category = BookCategory.objects.get(category_id=category_id)
        status = BookCode.objects.get(code_id=book_status)
        BookData.objects.filter(id=book_id).update(name=book_name, category=category, author=author, publisher=publisher, publish_date=publish_date, summary=summary, price=price, keeper_id=borrower_id, status=status)

        if borrower_id:
            borrower = Student.objects.get(id=borrower_id)
            lend_record = BookLendRecord(book=book, borrower=borrower, borrow_date=datetime.now().date())
            lend_record.save()

        return redirect(reverse('BookDetails', args=[book.id]))
    
    return render(request, 'books/bookedit.html', locals())


@login_required(login_url='/login/')
def book_details(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    keeper_name = None

    if book.keeper_id:
        keeper = get_object_or_404(Student, id=book.keeper_id)
        keeper_name = keeper.username

    return render(request, 'books/details.html', {'book': book, 'keeper_name': keeper_name})


@login_required(login_url='/login/')
def book_lendrec(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    lend_records = BookLendRecord.objects.filter(book=book).order_by('-id')
    
    return render(request, 'books/booklendrec.html', locals())