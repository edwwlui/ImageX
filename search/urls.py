from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='search_index'),
    path('image/<slug:search_type>', views.searchImage, name='search_Image'),
    path('browse', views.browse, name='browse_image')
    #path('search/gallery', views.searchGallery, name='search_Gallery')
]