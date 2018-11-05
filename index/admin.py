from django.contrib import admin, messages
from django.contrib.auth.models import User
from .models import Member, Image, Gallery, Curator, ResetPasswordRequest
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.admin.utils import unquote
from django.urls import path
from django.http import Http404, HttpResponseRedirect

# Register your models here.
class ResetPasswordRequestAdmin(admin.ModelAdmin):
	def reset_password(self, request, id):
		obj=ResetPasswordRequest.objects.filter(id=id)[0]
		if(obj.sent==True):
			messages.error(request, 'this request was already entertained')
			return HttpResponseRedirect('..')
		email = obj.email
		print(email)
		form = PasswordResetForm(data={'email': email})
		form.is_valid()
		form.save(email_template_name='registration/password_reset_email.html')
		obj.sendEmail()
		return HttpResponseRedirect('..')
	def get_urls(self):
		return [
			path('<id>/reset_password/',self.admin_site.admin_view(self.reset_password), name="auth_user_reset_password")
        ] + super().get_urls()


admin.site.register(ResetPasswordRequest, ResetPasswordRequestAdmin)
admin.site.register(Member)
admin.site.register(Image)
admin.site.register(Gallery)
admin.site.register(Curator)