from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # Login user
            login(request, user)
            return redirect('articles:blog')
    else:
        user_form = UserCreationForm()
    return render(request, 'users/signup.html', { 'form':user_form })

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            # Get user from form
            user = login_form.get_user()
            # Login user
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:blog')
    else:
        login_form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form':login_form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:blog')
