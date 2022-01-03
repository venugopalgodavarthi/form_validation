from django.forms import ValidationError

def minchar(value):
    if len(value)< 3:
        raise ValidationError('minimum 3 character')
    
def maxchar(value):
    if len(value)> 15:
        raise ValidationError('maximum 15 character, currently you enterd charaters are {}'.format(len(value)))
    
def starts_with_cap(value):
    if not(value[0].isupper()):
        raise ValidationError('first charcater should be uppercase')

def min18(value):
    if value<18:
        raise ValidationError('min 18 +') 