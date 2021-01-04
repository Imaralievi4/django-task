from django import forms 
from django.core.exceptions import ValidationError 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ToDoList

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'slug', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'input-group-text'}),
            
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create" ')
        return new_slug


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']