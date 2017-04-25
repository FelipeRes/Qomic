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
	sinopse = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'size': '100'}))
	capa = forms.ImageField(label='Capa',widget=forms.FileInput())
	ativada = forms.BooleanField(label='Disponibilizar')

class AlterarObra(forms.Form):
	nome = forms.CharField(max_length=50)
	sinopse = forms.CharField(max_length=500,required=False)
	capa = forms.ImageField(label='Seleciona uma imagem de capa',widget=forms.FileInput(),required=False)
	ativada = forms.BooleanField(label='Disponibilizar',required=False)

class NovoCapitulo(forms.Form):
	nome = forms.CharField(max_length=50)
	capa = forms.ImageField(label='Capa',widget=forms.FileInput())
	disponivel = forms.BooleanField(label='Disponibilizar',required=False)

class AlterarCapitulo(forms.Form):
	nome = forms.CharField(max_length=50)
	capa = forms.ImageField(label='Seleciona uma imagem de capa',widget=forms.FileInput(),required=False)
	disponivel = forms.BooleanField(label='Disponibilizar',required=False)

class NovaPagina(forms.Form):
	pagina = forms.ImageField(widget=forms.FileInput(),required=True)