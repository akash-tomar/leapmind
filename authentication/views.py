# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import *
from leapmind.settings import EMAIL_HOST_USER
import uuid
from .models import *
import datetime

# Create your views here.
class LoginView(View):
	template_name = 'login.html'
	form = LoginForm

	def get(self, request):
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse("worker:home"))
		
		form = self.form()
		if "recovery" in request.GET:
			if request.GET["recovery"]=="1":
				return render(request,self.template_name,{"form":form,"recovery":True})
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

class EmailView(View):

	template_name = "email.html"

	def get(self,request):
		return render(request,self.template_name,{})

	def post(self,request):
		email = request.POST["email"]
		user = User.objects.filter(email=email)[0]
		token = str(uuid.uuid4().get_hex())

		recovery_token = RecoveryToken(email=email,token=token)
		recovery_token.save()

		message = "http://localhost:8000/auth/recovery?email="+email+"&token="+token
		send_mail('LeapMind password recovery', message, EMAIL_HOST_USER,[email,], fail_silently=False)
		return render(request,self.template_name,{"success":True})	

class RecoveryView(View):
	
	template_name = "password_reset.html"

	def get(self,request):
		if "token" in request.GET:
			token = request.GET["token"]
			email = request.GET["email"]
			user = User.objects.filter(email=email)[0]
			try:
				recovery_token = RecoveryToken.objects.get(email=email)
				timediff = datetime.datetime.now() - recovery_token.timestamp.replace(tzinfo=None)
				timediff = timediff.seconds
				if timediff<=1800 and (recovery_token.token == token):
					return render(request,self.template_name,{"email":email})
			except:
				return HttpResponseRedirect(reverse("authentication:login"))
		return HttpResponseRedirect(reverse("authentication:login"))
		
	def post(self,request):
		email = request.POST.get("email")
		password = request.POST.get("password")
		confirm_password = request.POST.get("confirm_password")
		if password!=confirm_password:
			return render(request,self.template_name,{"passwords_dont_match":True})
		user = User.objects.filter(email=email)[0]
		recovery_token = RecoveryToken.objects.get(email=email)
		timediff = datetime.datetime.now() - recovery_token.timestamp.replace(tzinfo=None)
		timediff = timediff.seconds
		if timediff<=1800:
			recovery_token.delete()
			user.set_password(password)
			user.save()
			return HttpResponseRedirect(reverse("authentication:login")+"?recovery=1")
		return HttpResponseRedirect(reverse("authentication:login"))
