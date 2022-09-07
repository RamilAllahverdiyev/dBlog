from cmath import log
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
def registerPage(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}')
            return redirect('blog-home')
        else:    
            messages.error(request, 'An error occured during the registration')
            
    return render (request, 'blog/register.html', {'form': form})

def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    about = 'about'
    context = {'title':about}
    return render(request, 'blog/about.html', context)   