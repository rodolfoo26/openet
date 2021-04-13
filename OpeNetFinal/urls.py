"""OpeNetAluno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from core.views import register_new_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name = 'login'),
    path('pet/all/', views.list_login),
    path('login/submit', views.submit_login),
    path('register/', register_new_user.as_view(),name='registrar'),
    path('aluno/register/', views.register_aluno),
    path('aluno/register/submit', views.set_aluno),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='pet/all/'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
