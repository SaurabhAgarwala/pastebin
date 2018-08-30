from django.shortcuts import render, redirect
from .models import Content
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        e_url = request.POST.get('slug')
        if form.is_valid():
            s_instance = form.save(commit=False)
            s_instance.slug =  e_url
            s_instance.save()
        return render(request, 'posts/post_url.html', {'e_url':e_url})
    else:
        form = forms.PostForm
    pastes = Content.objects.all()
    pastes = sorted(pastes,key=lambda x:x.date,reverse=True)
    return render(request, 'posts/post_create.html', {'form':form, 'pastes':pastes})

def paste_disp(request, url):
    paste = Content.objects.get(slug=url)
    if paste.editable==True:
        return redirect('posts:edit', id=paste.id)
    return render(request, 'posts/post_disp.html', {'paste':paste})

@login_required(login_url="/accounts/login/")
def login_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        e_url = request.POST.get('slug')
        if form.is_valid():
            s_instance = form.save(commit=False)
            s_instance.slug = e_url
            s_instance.user = request.user
            s_instance.save()
        return render(request, 'posts/loggedin_post_url.html', {'e_url':e_url})
    else:
        form = forms.PostForm
        all_pastes = Content.objects.all()
        all_pastes = sorted(all_pastes,key=lambda x:x.date,reverse=True)
    pastes = Content.objects.filter(user=request.user)
    pastes = sorted(pastes,key=lambda x:x.date,reverse=True)
    return render(request, 'posts/loggedin_post_create.html', {'form':form, 'pastes':pastes, 'all_pastes':all_pastes })

@login_required(login_url="/accounts/login/")
def login_paste_disp(request, url):
    paste = Content.objects.get(slug=url)
    if paste.user == request.user:
        return redirect('posts:edit', id=paste.id)
    return render(request, 'posts/post_disp.html', {'paste':paste})

def edit(request, id):
    paste = Content.objects.get(id=id)
    if request.method == 'POST':
        form = forms.PostEditForm(request.POST)
        e_url = paste.slug
        heading = paste.title
        s_editable = paste.editable
        edited = True
        paste.delete()
        if form.is_valid():
            s_instance = form.save(commit=False)
            s_instance.slug = e_url
            s_instance.title = heading
            s_instance.user = request.user
            s_instance.editable = s_editable
            s_instance.save()
        return render(request, 'posts/loggedin_post_url.html', {'e_url':e_url, 'edited':edited})
    else:
        form = forms.PostEditForm(instance=paste)
    return render(request, 'posts/edit.html', {'form':form, 'paste':paste})

@login_required(login_url="/accounts/login/")
def delete(request, id):
    if request.method == 'POST':
        paste = Content.objects.get(id=id)
        paste.delete()
    return redirect('posts:post_login_create')
