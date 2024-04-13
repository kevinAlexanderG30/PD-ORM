from django.forms import ModelForm
from .models import Autor, Book

class AutorForm(ModelForm):
    class Meta: 
        model = Autor
        fields = "__all__"

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"