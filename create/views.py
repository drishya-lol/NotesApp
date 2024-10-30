from django.shortcuts import render
from base.models import NoteCategory

# Create your views here.
def create(request):
    notesCategoryData = NoteCategory.objects.all()
    data2 = {'notesCategory': notesCategoryData}
    return render(request, "create.html", context = data2)