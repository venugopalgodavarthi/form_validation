from django import forms
import datetime


class registerFORM(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    







class registerform(forms.Form):
    name= forms.CharField(required=True,label="USERNAME",initial='pys')
    agree=forms.BooleanField(initial=True)
    date=forms.DateField(initial=datetime.date.today)
    time=forms.DateTimeField(initial=datetime.datetime.today)
    firstname=forms.CharField(max_length=10,min_length=10)
    age=forms.IntegerField(min_value=18, max_value=56)
    
    