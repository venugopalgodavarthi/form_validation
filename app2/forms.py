from django import forms
from app2.validation import *



class registerFORM(forms.Form):
    firstname=forms.CharField(validators=[minchar,maxchar,starts_with_cap])
    lastname=forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    age= forms.IntegerField(validators=[min18])
    
    '''
    def clean(self):
        inp=self.cleaned_data['firstname']
        if len(inp)<3:
            raise forms.ValidationError('the minimum no of characters should be 3')
        elif len(inp)>15:
            raise forms.ValidationError('the maxmium no of characters should be 15,currently you assign character is{}'.format(len(inp)))
    
        inp=self.cleaned_data['lastname']
        if len(inp)<3:
            raise forms.ValidationError('the minimum no of characters should be 3')
        elif len(inp)>15:
            raise forms.ValidationError('the maxmium no of characters should be 15,currently you assign character is{}'.format(len(inp)))

        inp=self.cleaned_data['username']
        if len(inp)<5:
            raise forms.ValidationError('the minimum no of characters should be 5 in USERNAME FIELD')
        elif len(inp)>15:
            raise forms.ValidationError('the maxmium no of characters should be 15,currently you assign character is{}'.format(len(inp)))
        elif not(inp[0].isupper()):
            raise forms.ValidationError('the first character should be uppercase')

        inp=self.cleaned_data['age']
        if inp<18:
            raise forms.ValidationError('the minimum age of the person should be 18')
        elif inp>56:
            raise forms.ValidationError('the maximum age of the person should be 56')
    
    def clean_firstname(self):
        inp=self.cleaned_data['firstname']
        if len(inp)<3:
            raise forms.ValidationError('the minimum no of characters should be 3')
        elif len(inp)>15:
            raise forms.ValidationError('the maxmium no of characters should be 15,currently you assign character is{}'.format(len(inp)))
        return inp
    
    def clean_lastname(self):
        inp=self.cleaned_data['lastname']
        if len(inp)<3:
            raise forms.ValidationError('the minimum no of characters should be 3')
        elif len(inp)>15:
            raise forms.ValidationError('the maxmium no of characters should be 15,currently you assign character is{}'.format(len(inp)))
        return inp
    
    def clean_username(self):
        inp=self.cleaned_data['username']
        if len(inp)<5:
            raise forms.ValidationError('the minimum no of characters should be 5')
        elif len(inp)>15:
            raise forms.ValidationError('the maxmium no of characters should be 15,currently you assign character is{}'.format(len(inp)))
        elif not(inp[0].isupper()):
            raise forms.ValidationError('the first character should be uppercase')
        return inp
    
    def clean_age(self):
        inp=self.cleaned_data['age']
        if inp<18:
            raise forms.ValidationError('the minimum age of the person should be 18')
        elif inp>56:
            raise forms.ValidationError('the maximum age of the person should be 56')
        return inp
    '''