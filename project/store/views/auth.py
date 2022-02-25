from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from project.store.forms import UserCreationForm

def register(request):
    """register a new user and make him authenticated"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            messages.info(request, "account created successfully")
            return redirect('books')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})