from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory

# Create your views here.
def home(request):
    notesObjData = Note.objects.all() # returns a list of objects
    data = {'notes': notesObjData} # dictionary with notes as key and notesObjData as value
    return render(request, "index.html", context = data) #context sends the data to the template

def create(request):
    notesCategoryData = NoteCategory.objects.all()
    data2 = {'notesCategory': notesCategoryData}
    return render(request, "create.html", context = data2)