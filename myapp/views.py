from multiprocessing import context
from tkinter import image_names
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from myapp.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    d={
        "name": "Arun",
        "age": 20,
        
    }

    li= ["Allen","Sreerag","Alwin","Allu"]

    for i in range(0,10):
        print(i)

    context = {'li': li}
        
    return render(request, 'myapp/index.html',context=context)

def new_one(request):
    return render(request, 'listing/new_one.html')

def my_place(request):
    return render(request, 'listing/my_place.html')

@login_required
def products(request):
    #p = Product.objects.filter(price__gt = 17000)
    p = Product.objects.all()
    context = {'products':p}
    return render(request, 'myapp/products.html',context=context)

def product_details(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    return render(request, 'myapp/product_details.html',context=context)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        
        p = Product(name=name,price=price,description=desc,image=image)
        p.save()
        
        
        return redirect('/myapp/products')

    return render(request, 'myapp/add_product.html')

def update_product(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}
    if request.method == 'POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.description = request.POST.get('desc')
       
        try:
            p.image = request.FILES['upload']
        except:
            pass    
        # p = Product(name=name,price=price,description=desc,image=image)
        p.save()
        
        
        return redirect('/myapp/products')

    return render(request, 'myapp/update_product.html',context=context)


def delete_product(request,id):
    p = Product.objects.get(id=id)
    context = {'p':p}

    if request.method == 'POST':
        p.delete()
        return redirect('/myapp/products')

    return render(request, 'myapp/delete_product.html',context=context)


