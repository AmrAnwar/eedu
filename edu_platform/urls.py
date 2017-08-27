"""edu_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token


from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url


# from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/news/', include("news.api.urls", namespace='news-api')),
    url(r'^users/', include("accounts.urls", namespace='users')),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
    url(r'^api/answers/', include("answers.api.urls", namespace='answers-api')),
    url(r'^api/asks/', include("asks.api.urls", namespace='asks-api')),
    url(r'^api/study/', include("study.api.urls", namespace='study-api')),
]
admin.site.site_header = "Mr Tawfiq App"
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
