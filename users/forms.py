from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserEditForm(forms.ModelForm):
	"""
	A form that edits a user.
	"""

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		# fields = '__all__'

	def save(self, commit=True):
		user = super(UserEditForm, self).save(commit=False)
		# user.set_password(self.cleaned_data["password1"])
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user

class ProfileEditForm(forms.ModelForm):
	"""
	A form to edit Profile data
	"""

	class Meta:
		model = Profile
		fields = ['phone_number', 'perm_address']
