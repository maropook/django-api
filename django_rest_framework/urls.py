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
from api.urls import router as api_router
from diary.urls import router as diary_router
from article.urls import router as article_router
from book.urls import router as book_router
from django.views.generic import RedirectView
from user.views import Login
urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(article_router.urls)),  # article 日記アプリ
    url('todo/', include(api_router.urls)),  # todoアプリ
    url('book/', include(book_router.urls)),  # rakuten


    url('blog/', include(blog_router.urls)),
    url('diary/', include(diary_router.urls)),

    url('todolist/', RedirectView.as_view(url='/static/index.html')),
    path('login/', Login.as_view()),
]
