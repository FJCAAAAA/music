"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from download import views
from django.contrib.staticfiles.views import serve
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'download'


# 解决关闭debug后静态页面找不到问题
def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

app_name = 'download'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index',),
    url(r'^search/$', views.search, name='search'),
    url(r'^goodluck/$', views.good_luck, name='goodluck'),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)