from django.forms import ModelForm
from .models import *

class AddBooksForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class AddAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"