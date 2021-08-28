"""django_rest_framework URL Configuration

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
from django.urls.conf import include
from django.conf.urls import url
from blog.urls import router as blog_router
from upload.urls import router as upload_router
from api.urls import router as api_router
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(blog_router.urls)),
    url('api2/', include(upload_router.urls)),
    url('api3/', include(api_router.urls)),
    url('', RedirectView.as_view(url='/static/index.html')),

]
