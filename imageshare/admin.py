from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Image)

# now we can access this tables in as admin and fill something to them 
#  registering a model/table is imp otherwise we won't be able to access it from the admin panel