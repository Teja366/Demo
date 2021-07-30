from django.shortcuts import render, redirect  
from frontpage.forms import ProductForm  
from frontpage.models import Product 

# Create your views here.
 
#This is insertion code  

def pro(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form}) 

#This Code is to retrive the information from database

def show(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'product':products})  

#This code is to update the information

def edit(request, id):
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})   
    

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request,'edit.html', {'product': product})  

def destroy(request, id):  
    product = Product.objects.get(id=id)
    product.delete()  
    return redirect("/show") 

