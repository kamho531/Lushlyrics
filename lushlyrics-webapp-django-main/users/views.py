from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.models import playlist_user
from .forms import SignUpForm

# Create your views here.

def userlogin(request):
    user = playlist_user.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Log in success!")
            return redirect('default')
        else:
            messages.success(request, "Error! please try again!")
            return redirect('login')
    else:        
        return render(request, 'users/login.html', {'user': user})



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration success")
            return redirect('userlogin')
    else:
        form = SignUpForm()
        return render(request, 'users/register.html', 
                  {'form': form})   
    return render(request, 'users/register.html', 
                  {'form': form})



def userlogout(request):
    logout(request)
    messages.success(request, "You have logged out!")
    return redirect('userlogin')
