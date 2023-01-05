from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        
        model = Post
        fields = ['title', 'description', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control bg-dark w-85 text-white'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark w-85 text-white'}),
            'picture': forms.FileInput(attrs={'class': 'form-control bg-dark w-85 text-white'}),
        }
        labels = {
            'title': 'title',
            'description': 'description',
            'picture': 'picture'
        }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control bg-dark w-100 text-white'})
        }