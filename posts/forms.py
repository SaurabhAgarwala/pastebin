from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = ['title', 'body', 'editable']

class PostEditForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = ['body']
