from django.shortcuts import render,HttpResponse
from Home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    #return HttpResponse("THis is Home page")
    context={
        'variable1':"this variable is sent ",
        'variable2':"this is variable2 "
    }
    
    return render(request,'index.html',context)

def product(request):
    return render(request,'product.html')

    #return HttpResponse("THis is about page")

def services(request):
    return render(request,'services.html')

    #return HttpResponse("THis is services page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,phone=phone,address=address,message=message)
        contact.save()
        messages.success(request, "your message has been sent!!")
        
    return render(request,'contact.html')

    #return HttpResponse("THis is contact page")
    
def cart(request):
    return render(request,'cart.html')


#makemigrations=crate changes and store in a file
#migrate=apply the pending changes created by makemigrations