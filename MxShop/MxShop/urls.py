"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.contrib import admin
from django.urls import path,include,re_path
from MxShop.settings.base import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views





urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 富文本编辑器
    re_path(r'^ueditor/',include('DjangoUeditor.urls')),
    #静态文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),

    # 自动生成API文档
    re_path(r'^docs/', include_docs_urls(title="用户信息API文档")),

    # api浏览页
    re_path(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),


    re_path(r'^',include('goods.urls')),
    # re_path(r'^',include('users.urls',namespace='users')),

    # 用户认证
    re_path(r'^api-token-auth/', views.obtain_auth_token),

    # jwt认证
    path('login/', obtain_jwt_token),


]
