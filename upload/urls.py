from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index')
    #path('uploadImage/', views.uploadImage, name='uploadImage')
    #url(r'^upload/', views.uploadImage, name='upload')
]