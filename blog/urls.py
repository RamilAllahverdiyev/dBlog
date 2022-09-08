from os import stat
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.registerPage, name='blog-register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='blog-logout'),
    path('profile/', views.profile, name='blog-profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    )