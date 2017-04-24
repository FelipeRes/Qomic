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
	capa = forms.ImageField(label='Seleciona uma imagem de capa',widget=forms.FileInput())
	ativada = forms.BooleanField(label='Disponibilizar visualização')

class AlterarObra(forms.Form):
	nome = forms.CharField(max_length=50)
	sinopse = forms.CharField(max_length=500,required=False)
	capa = forms.ImageField(label='Seleciona uma imagem de capa',widget=forms.FileInput(),required=False)
	ativada = forms.BooleanField(label='Disponibilizar visualização',required=False)