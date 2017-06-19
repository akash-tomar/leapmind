# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
class LoginView(View):
	def get(self, request):
		return HttpResponse("blah")

	def post(self, request):
		return HttpResponse('result')

class SignupView(View):
	def post(self, request):
		return HttpResponse("blah")
	def get(self, request):
		return HttpResponse("blah")