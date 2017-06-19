from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)

	def __init__(self,*args,**kwargs):
		super(LoginForm,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'placeholder':'Username'})
		self.fields['password'].widget.attrs.update({'placeholder':'Password'})


class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password']

	def __init__(self,*args,**kwargs):
		super(SignupForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder':'First name'})
		self.fields['last_name'].widget.attrs.update({'placeholder':'Last name'})
		self.fields['username'].widget.attrs.update({'placeholder':'Username'})
		self.fields['email'].widget.attrs.update({'placeholder':'Email'})
		self.fields['password'].widget.attrs.update({'placeholder':'Password'})
