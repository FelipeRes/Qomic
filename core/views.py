from . import forms, models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
	if request.user.is_authenticated():
		context = {'login':True,}
		return render(request, 'index.html',context)
	else:
		if request.method == 'POST':
			form = forms.UsuarioLogin(request.POST)
			if form.is_valid():
				nomeUsuario = form.cleaned_data['nome']
				senha = form.cleaned_data['senha']
				user = authenticate(username=nomeUsuario, password=senha)
				if user is not None:
					if user.is_active:
						logout(request)
						login(request, user)
						return HttpResponseRedirect(reverse(index))
				else:
					context = {'form': form,
						'loginMessage':'Usuario ou senha estao incorretos',
						'messageColor':'red',
						'login':False,
						}
					return render(request, 'index.html',context)
		else:
			form = forms.UsuarioLogin()
			context = {'form': form,'login':False,}
			return render(request, 'index.html',context)

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
				return render(request,'cadastrarUsuario.html',{'form': form,'exception':'Nome de usuario ja existe'})
			return HttpResponseRedirect(reverse(index))
	else:
		form = forms.UsuarioForm()
	return render(request,'cadastrarUsuario.html',{'form': form,})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse(index))

@login_required
def profile(request):
	if request.user.is_authenticated():
		usuario = User.objects.get(username=request.user.username)
		contexto = {'obras':models.Obra.objects.filter(usuario=usuario)}
		return render(request,'profile.html',contexto)

@login_required
def nova_obra(request):
	if request.method == 'POST':
		form = forms.NovaObra(request.POST)
		if form.is_valid():
			usuario = User.objects.get(username=request.user.username)
			nomeObra = form.cleaned_data['nome']
			sinopse = form.cleaned_data['sinopse']
			obra = models.Obra(usuario=usuario,nomeObra=nomeObra,sinopse=sinopse,ativada=False)
			obra.save()
			return HttpResponseRedirect(reverse(profile))
		else:
			return HttpResponse("Ocorreu algum erro")
	else:
		form = forms.NovaObra()
		return render(request,'criarObra.html',{'form': form,'usuario':request.user.username})

