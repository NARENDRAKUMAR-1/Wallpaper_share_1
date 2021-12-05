from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#  now we are inside the models of an app, 
#  the models is to work with the db part
#  create class for an entity to work with

#categories model

class Category(models.Model):
    # this Model class is main thing , it's inside the models module
    #  models.Model this is done for every class

    title=models.CharField(max_length=100)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # so here, we have simply created the table to store all this props or columns of the Category table 

    def __str__(self):  # it's magic function which is auto called,, we must define it and return what we want the 
        # entry name to look like
        # if we don't specify anything then it'll show the object1, object2 like this
        return self.title

class Image(models.Model):

    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='media') # just look what we want and use that
                                                #  particular datatype to store the prop
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    # we will link this image with a category by foreignkey relationship

    # CASCADE is db part that when we'll delete a particular category all the images related to it will also be deleted

    # this props of the class are simply the what we want part
    # we will use this class names and the props while fetching the values stored inside them

    def __str__(self):  # special magic methods
        return self.title


