from django import forms
from .models import BookCategory, Student, BookCode

class BookSearchForm(forms.Form):
    book_title = forms.CharField(label='書名', required=False)
    category = forms.ModelChoiceField(queryset=BookCategory.objects.all(), label='書籍類別', empty_label='全部', required=False)
    borrower = forms.ModelChoiceField(queryset=Student.objects.all(), label='借閱人', empty_label='全部', required=False)
    status = forms.ModelChoiceField(queryset=BookCode.objects.all(), label='借閱狀態', empty_label='全部', required=False)
