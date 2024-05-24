from django.shortcuts import render,redirect

# Create your views here.

from .models import Book
from .forms import BookForm,AuthorForm


def createbook(request):
    books=Book.objects.all()
    if request.method=='POST':
        form = BookForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            
    else:
        form = BookForm()
    return render(request,'index.html',{'form':form,'books':books})

def detailedview(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailedview.html',{'book':book})

def updatebook(request,book_id):
    
    book=Book.objects.get(id=book_id)
    
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        
        book.title=title
        book.price=price
        
        book.save()
        
        return redirect('/')
    
    return render(request,'updatebook.html',{'book':book})


def deletebook(request,book_id):
    
    book=Book.objects.get(id=book_id)

    if request.method=='POST':
        
        book.delete()
        
        return redirect('/')
    return render(request,'deletebook.html',{'book':book})

def createauthor(request):
    if request.method=='POST':
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/')
    else:
        form=AuthorForm()
        
    
    return render(request,'author.html',{'form':form})
       
    
    