from django.forms import ModelForm
from  django import  forms
from .models import Comments

class CommentsForm(ModelForm):
     class Meta:
        model = Comments
        fields = ['message', 'name', 'email']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control w-100', "cols":"30", "rows":"9"}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }


