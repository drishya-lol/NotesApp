from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import CreateNoteForm, CreateNoteCategoryForm
from  django.shortcuts import redirect

# Create your views here.
def home(request):
    notes_obj = Note.objects.all()
    noteCategory_obj = NoteCategory.objects.all()
    data = {'notes': notes_obj, 'noteCategories': noteCategory_obj}
    return render(request, 'index.html', context=data)

def createNote(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'createNote.html', context = {'form': form})
    form = CreateNoteForm()
    data = {'form': form}
    return render(request, 'createNote.html', context=data)

def createCategory(request):
    if request.method == 'POST':
        form = CreateNoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'createCategory.html', context = {'form': form})
    form = CreateNoteCategoryForm()
    data = {'form': form}
    return render(request, 'createCategory.html', context=data)