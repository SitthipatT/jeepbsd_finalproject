from django import forms
from django.forms import ModelForm
from .models import NotePost

class PostForm(ModelForm):

    #is_good_day = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta: 
        model = NotePost
        fields = ('is_good_day','reason')

        widgets = {
            'is_good_day': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),

        }

