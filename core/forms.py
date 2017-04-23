from django import forms

class UsuarioForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)

class UsuarioLogin(forms.Form):
    nome = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)

class NovaObra(forms.Form):
	nome = forms.CharField(max_length=50)
	sinopse = forms.CharField(max_length=500)