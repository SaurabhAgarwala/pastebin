from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    password1 = forms.CharField(required=True, max_length=100)
    password2 = forms.CharField(required=True, max_length=100)
