from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Comment
rep="none";
user='none';

class ContactUs(forms.Form):
	name=forms.CharField(label='Name')
	email=forms.EmailField(label='Email')
	subject=forms.CharField(label='Subject')
	message=forms.CharField(label="Message",widget=forms.Textarea(attrs={'cols': 100, 'rows': 4}))
class ChangePassword(forms.ModelForm):
	username = forms.CharField(label='username')
	old=forms.CharField(label='old password', widget=forms.PasswordInput)
	newpass=forms.CharField(label='new password', widget=forms.PasswordInput)
	newpass2=forms.CharField(label='confirm password', widget=forms.PasswordInput)
	class Meta:
		model=User;
		fields=['username','old','newpass','newpass2']
	def clean_username(self):
		username=self.cleaned_data.get('username')
		return username
	def clean_old(self):
		old=self.cleaned_data.get('old')
		username=self.cleaned_data.get('username')
		new_user=authenticate(username=username,password=old)
		if new_user is None:
	 		raise forms.ValidationError("Incorrect Password")
	 	else:
			return old
	def clean_newpass(self):
		global rep
		rep=self.cleaned_data.get('newpass')
		if len(rep)<5:
	 		raise forms.ValidationError("weak password ")
		return rep
	def clean_newpass2(self):
	 	repassword=self.cleaned_data.get('newpass2')
	 	global rep;
	 	if(repassword!=rep):
	 	 	raise forms.ValidationError("password not same")
	 	return repassword


class SignUpForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	username = forms.CharField( label='username')
	email = forms.CharField( label='email')
	repassword=forms.CharField( label='confirm password' ,widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['email','username','password','repassword']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		try:
			User.objects.get(email=email)
		except ObjectDoesNotExist:
			return email
		raise forms.ValidationError('This email is already registered.')


	def clean_username(self):
		username = self.cleaned_data.get('username')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')

	def clean_password(self):
		global rep
		rep=self.cleaned_data.get('password')
		if len(rep)<5:
	 		raise forms.ValidationError("weak password ")
		return rep
	def clean_repassword(self):
	 	repassword=self.cleaned_data.get('repassword')
	 	global rep;
	 	if(repassword!=rep):
	 	 	raise forms.ValidationError("password not same")
	 	return repassword

	 	
class SignInForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	username = forms.CharField(label='username')
	class Meta:
		model=User
		fields=['username','password']
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			raise forms.ValidationError("Username doesn't exist.")
		return username
	
	def clean_password(self):
		passw=self.cleaned_data.get('password')
		username = self.cleaned_data.get('username')
		user=User.objects.get(username=username)
		if user is not None:
			new_user=authenticate(username=user,password=passw)
		if new_user is None:
	 		raise forms.ValidationError("Incorrect Password")
	 	else:
			return passw
class CommentForm(forms.ModelForm):
	comment= forms.CharField(label="",widget=forms.Textarea(attrs={'cols': 100, 'rows': 4}))
	class Meta:
		model=Comment
		fields=['comment']