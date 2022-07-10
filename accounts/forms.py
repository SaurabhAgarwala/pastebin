from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)
    confirm_password = forms.CharField(max_length=200, required=True)

    def __str__(self):
        return self.name

class LogInForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)

    def __str__(self):
        return self.name

