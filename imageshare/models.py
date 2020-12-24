from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#categories model

class Category(models.Model):

    title=models.CharField(max_length=100)
    description=models.TextField()

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):  # special magic methods
        return self.title


