from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.http import HttpResponse

from  imageshare.models import *

from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def about(request): # here we take request from the client along with the arguments from him if any
    #return HttpResponse('wallpapers')

    name='narendra'
    job='webdev'

    dict_1={
        'name':name,
        'job':job,
    }                           # the data is passed from the views to html like this
    #  either of dict or direct w/o dict...
    return render(request,'about.html',dict_1) # this dictionary is used for database related activities...
    #  before adding the html file here make sure to add the templates folder in settings

    #  whatever is output of our business logic, if we want to show it on frontend we must pass it using some dictionary 
    #  we can use direct variables too if count is less
    # pass the var in return so that it can be fetched on the frontend.....

    # dictionary name can be anything "context" is mostly followed


def homepage(request):

    images=Image.objects.all()
    cats=Category.objects.all()
    #  we load all the images and category data here
    # now we can work with them

    data_as_dict={
        'images':images,
        'cats':cats,
    }
    return render(request,'home.html',data_as_dict)

def show_category(request, cid):
    # this cid is used to show a particular category images only
    print(cid)
    cats=Category.objects.all()

    category=Category.objects.get(pk=cid)
    # pk here is required
    print(category)

    images=Image.objects.filter(cat=category)
    # this is imp it filtetrs the category based on cid -> category name

    data={
        'images':images,
    }

    return render(request, 'home.html' ,data)
    
def home(request):
    return redirect('/home')
    # the 1st page we want is the home page itself
    #  so redirect it to the home page


def register(request):

    form=UserCreationForm()
    # dict_form={
    #     'form':form,
    # }

    return render(request,'registerapp.html',{"form":form})

