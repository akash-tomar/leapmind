from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self,*args,**kwargs):
		super(LoginForm,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'placeholder':'Username'})
		self.fields['password'].widget.attrs.update({'placeholder':'Password','type':'password'})


class SignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email']

	def __init__(self,*args,**kwargs):
		super(SignupForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder':'First name'})
		self.fields['last_name'].widget.attrs.update({'placeholder':'Last name'})
		self.fields['username'].widget.attrs.update({'placeholder':'Username'})
		self.fields['email'].widget.attrs.update({'placeholder':'Email'})
		self.fields['password'].widget.attrs.update({'placeholder':'Password'})
		self.fields['confirm_password'].widget.attrs.update({'placeholder':'Confirm Password'})