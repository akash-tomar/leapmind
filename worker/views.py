# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
class HomeView(View):
	template_name = 'home.html'

	def get(self, request):
		if request.user.is_anonymous():
			return HttpResponseRedirect(reverse("authentication:login"))
		return render(request,self.template_name,{})
