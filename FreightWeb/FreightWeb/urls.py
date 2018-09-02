"""FreightWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url, include
from account import urls as account_urls
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from account import views as account_views




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet)
router.register(r'groups', account_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('^', include(router.urls)),
    # path('^api-auth/', include('rest_framework.urls'))
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
