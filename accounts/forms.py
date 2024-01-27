from django import forms
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth.models import User
from .models import profile
class Signupform(UserChangeForm,UserCreationForm):
    
    class Mete:
        model = User
        fields =['username','email','passward1','password']








class UserActivateform(forms.Form):
    code= forms.CharField(max_length=8)
    
    
    
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = profile
        fields = ['avatar', 'bio']