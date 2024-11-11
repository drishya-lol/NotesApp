from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import CreateNoteForm, CreateNoteCategoryForm
from  django.shortcuts import redirect

# Create your views here.
def home(request):
    notesObjData = Note.objects.all() # returns a list of objects
    noteCategoryObjs = NoteCategory.objects.all() # returns a list of objects
    data = {'notes': notesObjData , 'notecategory': noteCategoryObjs} # dictionary with notes as key and notesObjData as value
    return render(request, "index.html", context = data) #context sends the data to the template

def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'create_note.html', context ={'form': form})
    form = CreateNoteForm()
    data = {'form':form}
    return render(request, "create_note.html", context = data)

def create_category(request):
    if request.method == 'POST':
        form = CreateNoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'create_category.html', context={'form': form})
    form = CreateNoteCategoryForm()
    data = {'form': form}
    return render(request, "create_category.html", context = data)
        
def edit_category(request, pk):
    category = NoteCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateNoteCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'edit_category.html', context ={'form': form})
    form = CreateNoteCategoryForm(instance=category)
    data = {'form': form}
    return render(request, 'edit_category.html', data)
    
def edit_note(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'edit_note.html', context ={'form': form})
    form = CreateNoteForm(instance=note)
    data = {'form': form}
    return render(request, 'edit_note.html', data)
        
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    # if request.method == 'POST':
    note.delete()
    return redirect('home')
# return render(request, 'delete_note.html', {'note': note})

def delete_category(request, pk):
    notecategory = NoteCategory.objects.get(id=pk)
    notecategory.delete()
    return redirect('home')