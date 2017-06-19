# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render

# Create your views here.
class HomeView(View):
	template_name = 'home.html'

	def get(self, request):
		return render(request,self.template_name,{})
