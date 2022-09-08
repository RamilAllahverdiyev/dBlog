from cmath import log
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

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
            
    return render (request, 'blog/register.html', {'form':form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile(user=request.user)
    if request.method == 'POST':
       user_form = UserUpdateForm(request.POST, instance=request.user)
       profile_form = ProfileUpdateForm(
                  request.POST,
                  request.FILES,
                  instance=profile)
       if user_form.is_valid() and profile_form.is_valid():
           user_form.save()
           profile_form.save()
           messages.success(request, f'Your profile has been updated!')
           return redirect('blog-profile')    
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    
    context = {
        'user_form' : user_form,
        'profile_form': profile_form
    }
    return render(request, 'blog/profile.html', context )



def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    about = 'about'
    context = {'title':about}
    return render(request, 'blog/about.html', context)   