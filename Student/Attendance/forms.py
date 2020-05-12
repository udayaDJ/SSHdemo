from django import forms
from django.db.models.fields import CharField
from django.contrib.auth.models import User
class success(forms.Form):
 	username=forms.CharField(max_length=30,required=False)
 	password1=forms.CharField(max_length=30,required=True,widget=forms.PasswordInput)
	#register_no=forms.CharField(label='Enter The Register Number',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Register Number'}))

class add_det(forms.Form):
	name=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	register_no=forms.CharField(label='Enter The Register Number',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Register Number'}))
	dept=forms.CharField(label='Enter The Department',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Department'}))
	sec=forms.CharField(label='Enter The Section',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Section'}))
	phn_no=forms.CharField(label='Enter Phone Number',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))


class UploadFileForm(forms.Form):
	file = forms.FileField()

class phone(forms.Form):
	old_no=forms.CharField(label='Enter the Old Number',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Old Number'}))
	new_no=forms.CharField(label='Enter the new Number',max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'New Number'}))
class register(forms.Form):
	old_reg=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Old Register Number'}))
	new_reg=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'New Register Number'}))
class name(forms.Form):
	reg_num=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Register Number'}))
	name_update=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'Name To Update '}))
