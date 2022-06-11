from django.shortcuts import render, HttpResponse
from .models import *
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def hello(request):
    return render(request, 'chinchu.html',{"name": "cHinchu"})
def stud(request):
    std=Student.objects.all()
    return render(request,'chinchu.html',{'name':std})
def fun(request):
    obj=Student.objects.get(id=2)
    return render(request,'chinchu.html',{'name':obj})
def new(request):
    obj=Student.objects.filter(age=11)
    return render(request, 'chinchu.html',{'name':obj})
def web(request):
    obj=Student.objects.exclude(age=50)
    return render(request, 'chinchu.html',{'name':obj})
def base(request):
    obj=Student.objects.order_by("name")
    return render(request, 'chinchu.html',{'name':obj})

def update(request):
    obj=Student.objects.filter(name="rahul")
    obj.update(age=25)
    obj1=Student.objects.all()
    return render(request, 'chinchu.html',{'name':obj1})
def dele(request):
    obj=Student.objects.filter(name="coco")
    obj.delete()
    obj1=Student.objects.all()
    return render(request, "chinchu.html", {'name':obj1})
def mail(request):
    send_mail("new mail", "hai", "anchalimani@gmail.com", ["athenaerudition1@gmail.com"], fail_silently=False)
    return HttpResponse("SENT!!!!")

def message(request):
    EmailMessage("new mail", "hai", "anchuannmani@gmail.com", to=["athenaerudition1@gmail.com", "anchalimani@gmail.com"]).send()
    return HttpResponse("SENT!!!")

def email(request):
    mail=request.POST.get('email')
    sub=request.POST.get('sub')
    message=request.POST.get('message')
    email=EmailMessage("new mail", "hai", "anchuannmani@gmail.com", to["athenaeruditiion1@gmail.com", "anchuannmani@gmail.com"]).send()
    return render(request, "chinchu.html")

