from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.http import HttpResponse

from  imageshare.models import *

from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def about(request):
    #return HttpResponse('wallpapers')

    name='narendra'
    job='webdev'

    dict_1={
        'name':name,
        'job':job,
    }                           # the data is passed from the views to html like this
    return render(request,'about.html',dict_1) # this dictionary is used for database related activities...


def homepage(request):

    images=Image.objects.all()
    cats=Category.objects.all()

    data_as_dict={
        'images':images,
        'cats':cats,
    }
    return render(request,'home.html',data_as_dict)

def show_category(request, cid):
    print(cid)
    cats=Category.objects.all()

    category=Category.objects.get(pk=cid)
    print(category)

    images=Image.objects.filter(cat=category)

    data={
        'images':images,
    }

    return render(request, 'home.html' ,data)
    
def home(request):
    return redirect('/home')


def register(request):

    form=UserCreationForm()
    # dict_form={
    #     'form':form,
    # }

    return render(request,'registerapp.html',{"form":form})

