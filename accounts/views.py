from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def signup_view(request):
    error = {'label':'', 'message':'', 'error':False}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        error = update_error(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post_login_create')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_page.html', {'form':form, "error":error})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 's@next' in request.POST:
                return redirect(request.POST.get('s@next'))
            else:
                return redirect('posts:post_login_create')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_page.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post_create')

def update_error(form):
    error = {}
    try:
        err =form.errors.as_text().split("*")
        error['label'] = err[1]
        error['message'] = err[2].replace("This", "").replace("field", "Field")
        error['error'] = True
    except (IndexError):
        return error
    return error