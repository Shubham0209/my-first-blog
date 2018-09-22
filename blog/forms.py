from django import forms

from .models import Post

class PostForm(forms.ModelForm): #form name is PostForm and  tell Django that this form is a ModelForm

    class Meta:
        model = Post # which model should be used to create this form 
        fields = ('title', 'text',)