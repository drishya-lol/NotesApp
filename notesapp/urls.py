"""
URL configuration for notesapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from base.views import home, createNote, createCategory, editNote, editCategory, deleteNote, deleteCategory, register, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('createNote/', createNote, name='createNote'),
    path('createCategory/', createCategory, name='createCategory'),
    path('editNote/<int:id>/', editNote, name='editNote'),
    path('editCategory/<int:id>/', editCategory, name='editCategory'),
    path('deleteNote/<int:id>/', deleteNote, name='deleteNote'),
    path('deleteCategory/<int:id>/', deleteCategory, name='deleteCategory'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
