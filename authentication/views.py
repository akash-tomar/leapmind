# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import *


# Create your views here.
class LoginView(View):
	template_name = 'login.html'
	form = LoginForm

	def get(self, request):
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse("worker:home"))

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

		return render(request,self.template_name,{"form":self.form(),"failed":"Wrong username or password"})


class SignupView(View):
	form = SignupForm
	template_name = 'signup.html'
	
	def get(self, request):
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse("worker:home"))

		form = self.form()
		return render(request,self.template_name,{"form":form})

	def post(self, request):
		form = self.form(request.POST)
		# import pdb; pdb.set_trace()
		if form.is_valid():
			data = form.cleaned_data
			username = data["username"]
			email = data["email"]
			password = data["password"]
			confirm_password = data["confirm_password"]
			first_name = data["first_name"]
			last_name = data["last_name"]

			if password!=confirm_password:
				return render(request,self.template_name,{"form":self.form(),"failed":"Passwords don't match"})

			user = User(first_name=first_name,last_name=last_name,email=email,username=username)
			user.set_password(password)
			user.is_active=True
			user.save()

			auth = authenticate(username=username,password=password)

			if auth is not None:
				if auth.is_active:
					login(request,auth)
					return HttpResponseRedirect(reverse('worker:home'))			
					
		if "email" in form.errors:
			return render(request,self.template_name,{"form":self.form(),"failed":"This email already exists"})
				
		return render(request,self.template_name,{"form":self.form(),"failed":"Invalid fields for signup"})

class LogoutView(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect(reverse("authentication:login"))