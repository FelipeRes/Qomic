from . import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def index(request):
	context = {"Titulo": "Pagina Incial",}
	return render(request, 'index.html', context)

def usuario(request):
	if request.method == 'POST':
		form = forms.UsuarioForm(request.POST)
		if form.is_valid():
			nomeUsuario = form.cleaned_data['nome']
			email = form.cleaned_data['email']
			senha = form.cleaned_data['senha']
			try:
				user = User.objects.create_user(nomeUsuario, email, senha)
				user.save()
			except Exception as e:
				return render(request,'cadastrarUsuario.html',{'form': form,"Titulo":"Cadastre-se","exception":"Nome de usuario ja existe"})
			return HttpResponseRedirect(reverse(index))
	else:
		form = forms.UsuarioForm()
	return render(request,'cadastrarUsuario.html',{'form': form,"Titulo":"Cadastre-se"})