__author__ = 'Helder'

from django import forms


class FormContato(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea(), max_length=400)


