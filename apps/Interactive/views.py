from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory
from . import forms
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    user = None
    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            print(user.picture.url)
            print("a")
    else:
        form = forms.UserForm()
    return render(request, 'home.html', context={
        'form': form, 'user': user
    })

def show_tips(request):
    return render(request, 'tips.html')

def show_developer(request):
    return render(request, 'developer.html')