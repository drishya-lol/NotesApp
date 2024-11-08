from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory

# Create your views here.
def home(request):
    notesObjData = Note.objects.all() # returns a list of objects
    noteCategoryObjs = NoteCategory.objects.all() # returns a list of objects
    data = {'notes': notesObjData , 'notecategory': noteCategoryObjs} # dictionary with notes as key and notesObjData as value
    return render(request, "index.html", context = data) #context sends the data to the template
    