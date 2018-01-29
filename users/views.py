from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            # log the user in
            return redirect('articles:blog')
    else:
        user_form = UserCreationForm()
    return render(request, 'users/signup.html', { 'form':user_form })
