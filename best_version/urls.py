"""best_version URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from best_version import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'best_version'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('home', views.landing_page, name='landing_page'),
    path('current', views.current_page, name='current_page'),
    path('history', views.landing_page, name='landing_page')
]
urlpatterns += staticfiles_urlpatterns()
