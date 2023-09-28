from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile Number', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput (attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
