from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel, ProfileModel

class Register(forms.ModelForm):

    password = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'password'}))
    repassword = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'password'}))

    class Meta:
        model = UserModel
        fields = ['name', 'last_name', 'username', 'email', 'phone_number']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'text', 'name': 'name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'text', 'name': 'last_name'}),
            'username' : forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'text', 'name': 'username'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'text', 'name': 'email'}),
            'phone_number' : forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'type': 'text', 'name': 'phone_number'}),   
        }
        labels = {
            'name': 'name:',
            'last_name': 'last name',
            'username': 'username',
            'email': 'email',
            'phone_number': 'phone number'

        }

    def clean(self):

        cd = super().clean()
        print(cd)
        if cd['password'] != cd['repassword']:
            raise ValidationError("password are not match")
        
        return cd
    
    def save(self, commit=False):

        instance = super().save(commit)
        cd = super().clean()
        instance.set_password(cd['password'])
        instance.save()

class Login(forms.Form):

    username = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}))
    password = forms.CharField(max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white'}))

class ProfileEdit(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['profile_picture','about']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class':'form-control bg-dark text-white'}),
            'about': forms.Textarea(attrs={'class':'form-control bg-dark text-white'}),
        }