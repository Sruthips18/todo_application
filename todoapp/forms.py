from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todoapp.models import Todos

class UserForm(UserCreationForm):
     password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the password'}))
     password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm the password'}))
 
     class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the username'}),
            "email":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the email'}),
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'})
    #     self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
        

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the password'}))

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['name']
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control-inline','placeholder':'Enter the notes'}),
         }