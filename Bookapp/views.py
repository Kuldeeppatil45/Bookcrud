from django.shortcuts import render,redirect
from Bookapp.models import Book

# Create your views here.
def homepage(request):
    data = Book.objects.all()
    context = {}
    context['books'] = data
    return render(request,'home.html',context)

def addbook(request):
    if request.method=="GET":
        print("with in GET")        
        return render(request,'register.html')
    else:
        print("Within in POST")
        t = request.POST['title']
        a = request.POST['auther']
        p = request.POST['price']
        b = Book.objects.create(title=t,auther=a,price=p)
        b.save()
        #print("Bokk added",t,a,p)
        #return render(request,'home.html')
        return redirect("/home")
    
def deleteBook(request,bookid):
    b = Book.objects.filter(id = bookid)
    b.delete()
    return redirect("/home")

def updateBook(request,bookid):
    if request.method == "GET":
        #print("Updated book id",bookid)
        b = Book.objects.filter(id = bookid)
        context = {}
        context['book'] = b[0]
        return render(request,'updateBook.html',context)
    else:
        t = request.POST['title']
        a = request.POST['auther']
        p = request.POST['price']
        b = Book.objects.filter(id = bookid)
        b.update(title=t,auther=a,price=p)
        return redirect('/home')


