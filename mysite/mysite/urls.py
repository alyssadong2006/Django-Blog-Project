"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views #import views.py

urlpatterns = [
    #type in strings after the page line to get to the assigned page. For example:
    #http://127.0.0.1:8000/hello
    #or
    #http://127.0.0.1:8000/admin/
    #path('', {some function here}) will be the default path

    path('hello',views.index), #Add out index to the URL patterns
    path('admin/', admin.site.urls),
]
