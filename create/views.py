from django.shortcuts import render
from base.models import NoteCategory
from base.forms import CreateNoteForm, CreateNoteCategoryForm

# Create your views here.

def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
    form = CreateNoteForm()
    data = {'form':form}
    return render(request, "create_note.html", context = data)

def create_category(request):
    if request.method == 'POST':
        form = CreateNoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form = CreateNoteCategoryForm()
    data1 = {'form':form}
    return render(request, "create_category.html", context = data1)