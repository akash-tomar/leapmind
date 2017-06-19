# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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
		import pdb;pdb.set_trace()
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
			data = form.cleaned_data
			username = data["username"]
			email = data["email"]
			password = data["password"]
			first_name = data["first_name"]
			last_name = data["last_name"]

			user = User(first_name=first_name,last_name=last_name,email=email,username=username)
			user.set_password(password)
			user.is_active=True
			user.save()

			auth = authenticate(username=username,password=password)

			if auth is not None:
				if auth.is_active:
					login(request,auth)
					return HttpResponseRedirect(reverse('worker:home'))			

		return render(request,self.template_name,{"form":self.form()})