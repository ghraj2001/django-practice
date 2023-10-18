from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

def index(request):
   return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is aboutpage")

def services(request):
    return render(request,'service.html')
    # return HttpResponse("this is servicespage")

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        #date = datetime.now()
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Profile details stored.")
    return render(request,'contact.html')
    # return HttpResponse("this is contactpage")