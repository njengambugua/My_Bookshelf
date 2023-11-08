from django.shortcuts import render, redirect
from .models import Book
from .form import BookForm


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})


def list_book(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
