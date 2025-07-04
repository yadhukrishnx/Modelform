from django import forms
from .models import Book,Author

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model =Author
        fields=['name']
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields='__all__'