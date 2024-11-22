from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User

def register(request):
    # Check POST or GET
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, account OK!!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {"form": form})

def profile_page(request):
    # print("REQUEST =======", )
    user = User.objects.get(username=request.user)
    return render(request, 'users/profile.html', {"user": user})


