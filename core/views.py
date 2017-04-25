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
		context = {'login':True,'obras':models.Obra.objects.filter(ativada=True),'user':request.user.username}
	else:
		context = {'login':False,'obras':models.Obra.objects.filter(usuario=True),'user':request.user.username}
	return render(request, 'index2.html',context)

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

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse(index))

def user_login(request):
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
				return render(request, 'login.html',context)
	else:
		form = forms.UsuarioLogin()
		context = {'form': form,'login':False,}
		return render(request, 'login.html',context)

@login_required
def profile(request):
	if request.user.is_authenticated():
		usuario = User.objects.get(username=request.user.username)
		contexto = {'obras':models.Obra.objects.filter(usuario=usuario), 'user':usuario}
		return render(request,'profile.html',contexto)

@login_required
def nova_obra(request):
	if request.method == 'POST':
		form = forms.NovaObra(request.POST,request.FILES)
		if form.is_valid():
			usuario = User.objects.get(username=request.user.username)
			nomeObra = form.cleaned_data['nome']
			sinopse = form.cleaned_data['sinopse']
			capa = form.cleaned_data['capa']
			ativada = form.cleaned_data['ativada']
			obra = models.Obra(usuario=usuario,nomeObra=nomeObra,sinopse=sinopse,ativada=ativada,capa=capa)
			obra.save()
			return HttpResponseRedirect(reverse(profile))
		else:
			return HttpResponse(request.POST)
	else:
		form = forms.NovaObra()
		return render(request,'obra_form.html',{
			'form': form,
			'usuario':request.user.username,
			'action':'Criar Obra',
			'submeterAcao':'Criar Nova Obra',
			})

@login_required
def alterar_obra(request, obra_id):
	if request.method == 'POST':
		form = forms.AlterarObra(request.POST,request.FILES)
		if form.is_valid():
			usuario = User.objects.get(username=request.user.username)
			obra = models.Obra.objects.get(usuario=usuario,id=obra_id)
			if form.cleaned_data['nome'] is not None:
				obra.nomeObra = form.cleaned_data['nome']
			if form.cleaned_data['sinopse'] is not None:
				obra.sinopse = form.cleaned_data['sinopse']
			if form.cleaned_data['capa'] is not None:
				obra.capa = form.cleaned_data['capa']
			if form.cleaned_data['ativada'] is not None:
				obra.ativada = form.cleaned_data['ativada']
			obra.save()
			return redirect('/profile/obra/'+str(obra_id)+'/alterar/')
		else:
			return HttpResponse("Erro de envio de formulario")
	else:
		usuario = User.objects.get(username=request.user.username)
		obra = models.Obra.objects.get(usuario=usuario,id=obra_id)
		form = forms.AlterarObra(initial={
			'nome':obra.nomeObra,
			'sinopse':obra.sinopse,
			'capa':obra.capa,
			'ativada':obra.ativada,})
		return render(request,'obra.html',{
			'form': form,
			'usuario':request.user.username,
			'action':'Alterar Obra',
			'submeterAcao':'Salvar',
			'obra':obra,
			'capitulos':models.Capitulo.objects.filter(obra=obra_id),
			},)

@login_required
def deletar_obra(request, obra_id):
	usuario = User.objects.get(username=request.user.username)
	obra = models.Obra.objects.get(usuario=usuario,id=obra_id)
	obra.delete()
	return HttpResponseRedirect(reverse(profile))

@login_required
def novo_capitulo(request, obra_id):
	if request.method == 'POST':
		form = forms.NovoCapitulo(request.POST,request.FILES)
		if form.is_valid():
			obra = models.Obra.objects.get(id=obra_id)
			nomeCapitulo = form.cleaned_data['nome']
			capa = form.cleaned_data['capa']
			capitulo = models.Capitulo(obra=obra,nomeCapitulo=nomeCapitulo,disponivel=False,capa=capa)
			capitulo.save()
			return redirect('/profile/obra/'+str(obra_id)+'/alterar/')
		else:
			return HttpResponse("Ocorreu algum erro")
	else:
		form = forms.NovoCapitulo()
		return render(request,'capitulo_form.html',{
			'form': form,
			'action':'Criar Capitulo',
			'submeterAcao':'Criar Novo Capitulo',
			})

@login_required
def alterar_capitulo(request, capitulo_id):
	if request.method == 'POST':
		form = forms.AlterarCapitulo(request.POST,request.FILES)
		if form.is_valid():
			capitulo = models.Capitulo.objects.get(id=capitulo_id)
			if form.cleaned_data['nome'] is not None:
				capitulo.nomeCapitulo = form.cleaned_data['nome']
			if form.cleaned_data['capa'] is not None:
				capitulo.capa = form.cleaned_data['capa']
			if form.cleaned_data['disponivel'] is not None:
				capitulo.disponivel = form.cleaned_data['disponivel']
			capitulo.save()
			return redirect('/profile/capitulo/'+str(capitulo_id)+'/alterar/')
		else:
			return HttpResponse("Erro de envio de formulario")
	else:
		capitulo = models.Capitulo.objects.get(id=capitulo_id)
		form = forms.AlterarCapitulo(initial={
			'nome':capitulo.nomeCapitulo,
			'capa':capitulo.capa,
			'disponivel':capitulo.disponivel,})
		form2 = forms.NovaPagina()
		return render(request,'capitulo.html',{
			'form': form,
			'form2': form2,
			'action':'Alterar Capitulo',
			'submeterAcao':'Salvar',
			'capitulo':capitulo,
			'paginas': models.Pagina.objects.filter(capitulo=capitulo),
			},)

@login_required
def deletar_capitulo(request, capitulo_id):
	capitulo = models.Capitulo.objects.get(id=capitulo_id)
	capitulo.delete()
	return HttpResponseRedirect(reverse(profile))

@login_required
def inserir_pagina(request, capitulo_id):
	if request.method == 'POST':
		form = forms.NovaPagina(request.POST,request.FILES)
		if form.is_valid():
			capitulo = models.Capitulo.objects.get(id=capitulo_id)
			pagina = models.Pagina(pagina=form.cleaned_data['pagina'],capitulo=capitulo)
			pagina.save()
			return redirect('/profile/capitulo/'+str(capitulo_id)+'/alterar/')
		else:
			return HttpResponse("Ocorreu algum erro")
	else:
		return redirect('/profile/capitulo/'+str(capitulo_id)+'/alterar/')

@login_required
def deletar_pagina(request, pagina_id):
	pagina = models.Pagina.objects.get(id=pagina_id)
	capitulo = pagina.capitulo
	pagina.delete()
	return redirect('/profile/capitulo/'+str(capitulo.id)+'/alterar/')

@login_required
def ver_obra(request, obra_id):
	return render(request,'ver_obra.html',{
			'obra':models.Obra.objects.get(id=obra_id),
			'capitulos':models.Capitulo.objects.filter(obra=obra_id),
			},)

@login_required
def ver_capitulo(request, capitulo_id):
	return render(request,'ver_capitulo.html',{
			'capitulo':models.Capitulo.objects.get(id=capitulo_id),
			'paginas':models.Pagina.objects.filter(capitulo=capitulo_id),
			},)