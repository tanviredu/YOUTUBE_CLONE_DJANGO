from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile


class SignupForm(UserCreationForm):
    username   = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'username'}))
    email      = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    password1  = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2  = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))


    model = User
    fields = ('username','email','password1','password2')



class LoginForm(AuthenticationForm):
    username   = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'username'}))
    password   = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'password'}))

    class Meta:
        model  = User
        fields = ['username','password']



## profile model edit functionality
class EditProfile(forms.ModelForm):
    class Meta:
        model   = Profile
        exclude = ['user'] 
    