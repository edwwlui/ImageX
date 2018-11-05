from django import forms
from index import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError 

class PasswordResetForm(forms.ModelForm):
	email = forms.EmailField(label=("Email"), max_length=254, required=True)
	class Meta:
		model=models.ResetPasswordRequest
		fields = ['email']
	def clean_email(self):
		email = self.cleaned_data['email']
		if not User.objects.filter(email__iexact=email, is_active=True).exists():
			raise ValidationError("There is no user registered with the specified email address!")

		return email