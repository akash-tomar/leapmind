# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import *

# Create your views here.
class LoginView(View):
	template_name = 'login.html'
	form = LoginForm

	def get(self, request):
		form = self.form()
		return render(request,self.template_name,{"form":form})

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data["username"]
			password=data["password"]
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('worker:home'))

		return render(request,self.template_name,{"form":self.form()})


class SignupView(View):
	form = SignupForm
	template_name = 'signup.html'
	
	def get(self, request):
		form = self.form()
		return render(request,self.template_name,{"form":form})

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			user=authenticate(username=form.cleaned_data.data["username"]
					,password=form.cleaned_data.get["password"])
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('worker:home'))			

		return render(request,self.template_name,{"form":self.form()})