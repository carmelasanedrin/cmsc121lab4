from django.forms.widgets import DateTimeBaseInput
from library.forms import AddAuthorForm, AddBooksForm
from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    data = {"books": books, "authors": authors}
    return render(request, "library/home.html", data)


def addauthor(request):
    authorsform = AddAuthorForm()

    if (request.method == "POST"):
        authorsform = AddAuthorForm(request.POST)
        if (authorsform.is_valid()):
            authorsform.save()
            return redirect("/")
    data = {"authorsform" : authorsform }
    return render(request, 'library/addauthor.html', data)


def addbooks(request):
    booksform = AddBooksForm()

    if (request.method == "POST"):
        booksform = AddBooksForm(request.POST)
        if (booksform.is_valid()):
            booksform.save()
            return redirect("/")
    data = {"booksform" : booksform }
    return render(request, 'library/addbooks.html', data)


def updatebooks(request, pk):
    books = Book.objects.get(id=pk)
    booksform = AddBooksForm(instance=books)

    if (request.method == "POST"):
        booksform = AddBooksForm(request.POST, instance=books)
        if(booksform.is_valid()):
            booksform.save()
            return redirect("/")
    data = {"booksform": booksform }
    return render(request, 'library/updatebooks.html', data)


def updateauthor(request, pk):
    authors = Author.objects.get(id=pk)
    authorsform = AddAuthorForm(instance=authors)

    if (request.method == "POST"):
        authorsform = AddAuthorForm(request.POST, instance=authors)
        if(authorsform.is_valid()):
            authorsform.save()
            return redirect("/")
    data = {"authorsform": authorsform }
    return render(request, 'library/updateauthor.html', data)


def deletebook(request, pk):
    books = Book.objects.get(id=pk)
    books.delete() 
    return redirect("/")


def deleteauthor(request, pk):
    authors = Author.objects.get(id=pk)
    authors.delete() 
    return redirect("/")

