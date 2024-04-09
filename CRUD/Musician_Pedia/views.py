from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from Musician_Pedia.forms import WriterForm, BookForm, InduvidualsBookForm
from Musician_Pedia.models import Writer, Book
from django.db.models import Avg


# Create your views here.


def home(request):
    writer_list = Writer.objects.all().order_by('first_name')
    dictionary = {
        'title':'Home',
        'writer_list':writer_list,
    }
    return render(request, 'index.html', context=dictionary)

def add_writer(request):
    form = WriterForm()
    dictionary = {
        'title':'Add Writer',
        'form': form,
    }
    if request.method == 'POST':
        form = WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'writer_form.html', context=dictionary)

def add_book(request):
    form = BookForm()
    dictionary = {
        'title':'Add Book',
        'form': form,
    }
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
            
    return render(request, 'book_form.html', context=dictionary)


def book_list(request , id ):
    list_of_books = Book.objects.filter(name_id=id).order_by('release_date')
    writer = Writer.objects.get(pk=id )
    rate = Book.objects.filter(name_id=id).aggregate(Avg('book_ratings'))
    dictionary ={
        'title':'Book List',
        'list_of_books':list_of_books,
        'writer':writer,
        'rate':rate
    }
    return render(request, 'book_list.html', context=dictionary)


def update_book(request, book_id, id):
    writer = Writer.objects.get(pk=id)
    book = Book.objects.get(pk=book_id)
    form = BookForm(instance=book)
    dictionary = {
        'title': "Updating Book",
        'form': form,
    }
    if request.method == 'POST':
        form = BookForm( request.POST, instance= book )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Musician_Pedia:book_list', args=[id]))
    return render(request, 'update_book.html', context=dictionary)


def update_writer(request, id):
    writer = Writer.objects.get(pk=id)
    form = WriterForm(instance=writer)
    dictionary ={
        'title': "Updating Writer",
        'form': form,
    }
    if request.method == 'POST':
        form = WriterForm( request.POST, instance= writer )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'update_writer.html', context=dictionary)

def delete_writer(request , id):
    artist = Writer.objects.get(pk=id).delete()
    dictionary ={
        'title': "Delete Artist",
        'alert': "Sucessfully Deleted The Writer",
    }
    return render(request, 'delete.html', context=dictionary)


def delete_book(request, book_id):
    album = Book.objects.get(pk=book_id).delete()
    dictionary = {
        "title": "Delete Book",
        "alert": "Sucessfully Deleted The Book"
    }
    return render(request, 'delete.html', context=dictionary)

def add_individuals_book(request, id):
    form = InduvidualsBookForm()
    writer = Writer.objects.get(pk=id)
    if request.method == 'POST':
        form = InduvidualsBookForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.name = writer
            book.save()
            return HttpResponseRedirect(reverse('Musician_Pedia:book_list', args=[id]))
    dictionary = {
        'title':'Update Resource',
        'form':form,
        'writer':writer,
    }
    return render(request, 'add_individuals_book.html', context=dictionary)