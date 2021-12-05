"""imagebazaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
# the above 2 are for the media wala part

from registerapp import views as regview

from .views import * # required otherwise nothing will work as business logic itself resides in the views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('imageshare.urls') ),
    path('about/',about, name='about'),
    path('home/',homepage,name='homepage'),
    path('category/<int:cid>', show_category,name="show_category"),
    path('',home,name='home'),
    # path('register/',regview.register,name='register'),
    # path('register/',register,name='register'),
    path('', include('registerapp.urls') ),
    path('',include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  we setup 2 things in settings,  MEDIA_URl and MEDIA_ROOT,  
# specify those here
