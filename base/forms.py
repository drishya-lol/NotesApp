from django import forms
from .models import Note, NoteCategory
from django.contrib.auth.models import User

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note Name','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'category': forms.Select(attrs={'class': 'form-control','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            }
        
class CreateNoteCategoryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Note Category Name','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password','style': 'width: 50%; border-color: #000000; border-width: 1px; border-style: solid; border-radius: 5px;'}),
            }