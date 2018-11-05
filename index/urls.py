from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('', include('django.contrib.auth.urls')),
    path('image/<int:image_id>', views.viewImage, name='view_Image'),
    # path('image/all', views.viewImageAll, name='view_ImageAll'),
    # path('member/all', views.viewMemberAll, name='view_MemberAll'),
    path('image/<int:image_id>/delete',views.delete,name='delete'),
	path('image/<int:image_id>/download',views.download,name='download'),
	path('image/<int:image_id>/like',views.like,name='like'),
    path('viewProfile/<int:user_id>', views.viewProfile, name='view_Profile') 
]