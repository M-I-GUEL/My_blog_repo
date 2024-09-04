from django.urls import path
from django.conf import settings
from .views import base, posts,read,create_post,sign_up,log_in,log_out,profile
from django.conf.urls.static import static

urlpatterns = [
                path('post/', posts, name = 'posts'),
                path('base/', base, name='base'),
                path('read/<int:id>/', read, name ='read_detail'),
                path('create_post/', create_post, name='create_post'),
                path('sign_up/', sign_up, name='sign_up'),
                path('log_in/', log_in, name='log_in'),
                path('log_out/', log_out, name='log_out'),
                path('profile/', profile, name='profile') 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
