from django import forms
from .models import BookCategory, Student, BookCode

class BookSearchForm(forms.Form):
    book_title = forms.CharField(label='書名', required=False, initial='')
    category_id = forms.ModelChoiceField(queryset=BookCategory.objects.all(), label='書籍類別', empty_label='全部', required=False)
    borrower_id = forms.ModelChoiceField(queryset=Student.objects.all(), label='借閱人', empty_label='全部', required=False)
    book_status = forms.ModelChoiceField(queryset=BookCode.objects.all(), label='借閱狀態', empty_label='全部', required=False)
