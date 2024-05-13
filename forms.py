from  django import forms
from  .models import *

class regform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    age=forms.IntegerField()
    country=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)


class logform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)


class itemform(forms.Form):
    email=forms.EmailField()
    name=forms.CharField(max_length=20)
    # type=forms.CharField(max_length=20)

    type = forms.CharField(max_length=20)
    ingree=forms.CharField(max_length=2000)
    step=forms.CharField(max_length=3000)
    image=forms.ImageField()


# contactform
class contactform(forms.Form):
    email=forms.EmailField()
    subject=forms.CharField(max_length=40)
    message=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'row':3,'col':30}))

class review_form(forms.Form):
    ids=forms.CharField(max_length=10)
    name=forms.CharField(max_length=10)
    comment=forms.CharField(max_length=50)
    rate=forms.IntegerField()


