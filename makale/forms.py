from django.forms import ModelForm
from .models import Makale
from django import forms


class MakaleForm(ModelForm):
    class Meta:
        model=Makale
        fields = ['baslik','icerik','makale_foto']


