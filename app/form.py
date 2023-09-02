from django import forms
from . models import *

class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Add new tasks'}))

    class Meta:
        model = Todo
        fields = '__all__'
