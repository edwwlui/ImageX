from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
	url(r'^invitations/', include('invitations.urls'), name='invitations'),
	url(r'^register/$', views.register, name='register'),
	url(r'^change_password/', views.change_password, name='change_password'),
	url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
	url(r'^add_profile/', views.add_profile, name='add_profile')
]
