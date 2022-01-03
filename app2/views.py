from django.shortcuts import render
from django.http import HttpResponse
from app2.forms import registerFORM
# Create your views here.

def sample(request):
    return HttpResponse('this is app2 sample view')

def home(request):
    return render(request,'home2.html')


def register(request):
    form=registerFORM
    if request.method=='POST':
        form=registerFORM(request.POST)
        print('haii')
        print(form.is_valid())
        if form.is_valid():
            user=form.cleaned_data['username']
            print(user)
    return render(request,'register.html',{'form':form})
