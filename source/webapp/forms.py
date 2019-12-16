from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Image

class ImageForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=None, label='Автор', required=True, empty_label=None)

    class Meta:
        model = Image
        fields = ['image', 'text']