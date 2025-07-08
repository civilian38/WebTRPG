from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account-home')  # 성공 시 이동
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account-home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def account_home(request):
    if request.user.is_authenticated:
        return render(request, 'account/account_home.html', {'user': request.user})
    else:
        return render(request, 'account/account_home.html', {'user': None})