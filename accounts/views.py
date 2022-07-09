from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .models import PastBinUsers

from .forms import SignUpForm, LogInForm

# sign up user
def signup_view(request):
    submit_error = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # get  data from form
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password = form.cleaned_data['password']
            # check if username already exists and password aer the same
            if((password == password) and (not PastBinUsers.objects.filter(name=name).exists())):
                # add data to database
                PastBinUsers(name=name, password=password).save()
                # load the login page
                return render(request, 'accounts/login_page.html', {'form': form, 'submit_error': submit_error})
            else:
                submit_error = True
                # reload the signup page to display error
                return render(request, 'accounts/signup_page.html', {'form': form, 'submit_error': submit_error})
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup_page.html', {'form': form, 'submit_error': submit_error})


# log in user
def login_view(request):
    submit_error = False
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            # get data from form
            submit_error = True
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                # check if name is in database
                database = PastBinUsers.objects.get(name=name)
                if password == database.password:
                    return redirect('post_create')
                else:
                    submit_error = True
            except PastBinUsers.DoesNotExist:
                submit_error = True
    else:
        form = LogInForm()
    return render(request, 'accounts/login_page.html', {'form': form, 'submit_error': submit_error})

# log out user
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post_create')
