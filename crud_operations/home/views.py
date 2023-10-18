from django.shortcuts import render,redirect
from home.models import Employee

# Create your views here.
def index(request):
    if(request.method=='POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        emp = Employee(name=name,email=email,phone=phone,address=address)
        emp.save()
        redirect('home')
    emp = Employee.objects.all()
    context = {
        'emp':emp,
    }
    return render(request,'index.html',context)

def update(request,id):
    if(request.method=="POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        emp = Employee(id=id,name=name,email=email,phone=phone,address=address)
        emp.save()
        return redirect('home')
    return redirect(request,'index.html')

def delete(request,id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    return redirect("home")



        
