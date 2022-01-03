from django.shortcuts import render
class sample():
    pass
obj=sample()
obj.name="pyspider"
obj.address='bangalore'


def home(request):
    return render(request,'home.html',context={'data':100,
                                               'data1':[10,20,30,40],
                                               'data2':(10,'qsp'),
                                               'data3':{'A':100,'B':200},
                                               'data4':obj})