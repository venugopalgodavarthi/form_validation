from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import registerform
# Create your views here.

def sample(request):
    return HttpResponse("this is app1 sample view")

def home(request):
    return render(request,'home1.html')

def register(request):
    form=registerform()
    return render(request,'register.html',{'form':form})