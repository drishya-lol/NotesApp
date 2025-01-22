from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import CreateNoteForm, CreateNoteCategoryForm, UserForm
from  django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        notes_obj = Note.objects.all()
        noteCategory_obj = NoteCategory.objects.all()
        query = request.GET.get('query')
        if query:
            notes_obj = notes_obj.filter(name__icontains=query)
        data = {'notes': notes_obj, 'noteCategories': noteCategory_obj}
        return render(request, 'index.html', context=data)
    else:
        return redirect('login')

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

def editNote(request, id):
    note_obj = Note.objects.get(id=id)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'editNote.html', context = {'form': form})
    form = CreateNoteForm(instance=note_obj)
    data = {'form': form}
    return render(request, 'editNote.html', context=data)

def deleteNote(request, id):
    note_obj = Note.objects.get(id=id)
    note_obj.delete()
    return redirect('home')

def deleteCategory(request, id):
    noteCategory_obj = NoteCategory.objects.get(id=id)
    noteCategory_obj.delete()
    return redirect('home')

def editCategory(request, id):
    noteCategory_obj = NoteCategory.objects.get(id=id)
    if request.method == 'POST':
        form = CreateNoteCategoryForm(request.POST, instance=noteCategory_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'editCategory.html', context = {'form': form})
    form = CreateNoteCategoryForm(instance=noteCategory_obj)
    data = {'form': form}
    return render(request, 'editCategory.html', context=data)

def register(request):
    form = UserForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = make_password(password)
        data = request.POST.copy()
        data['password'] = new_password
        form = UserForm(data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'register.html', context = {'form': form})
    data = {'form': form}
    return render(request, 'register.html', context=data)

def user_login(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user == None:
            data = {'form': form, 'error': 'Invalid username or password'}
            return render(request, 'login.html', context = data)
        else:
            login(request, user)
            return redirect('home')
    data = {'form': form}
    return render(request, 'login.html', context=data)

def user_logout(request):
    logout(request)
    return redirect('home')