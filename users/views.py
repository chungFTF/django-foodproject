from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    # Check POST or GET
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, account OK!!')
            return redirect('food:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})

