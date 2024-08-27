from django.urls import path
from django.conf import settings
from .views import test, practice,read,create_post,sign_up,log_in,log_out,profile
from django.conf.urls.static import static

urlpatterns = [
                path('practice/', practice, name = 'practice'),
                path('test/', test, name='test'),
                path('read/<int:id>/', read, name ='read'),
                path('create_post/', create_post, name='create_post'),
                path('sign_up/', sign_up, name='sign_up'),
                path('log_in/', log_in, name='log_in'),
                path('log_out/', log_out, name='log_out'),
                path('profile/', profile, name='profile') 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
