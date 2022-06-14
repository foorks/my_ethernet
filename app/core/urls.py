"""core URL Configuration

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
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("layout.urls")),
    path("", include("news.urls")),
    path("", include("weathers.urls")),
    path("", include("currencies.urls")),
    path("", include("manga.urls")),
    path("", include("vk.urls")),
    path("", include("anime.urls")),
    path("", include("twitch.urls")),
    path("", include("youtube.urls")),
    path("", include("serials.urls")),
    path("", include("torrents.urls")),
    path("", include("hh.urls")),
    path("", include("dashboard.urls")),
]