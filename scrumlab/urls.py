"""scrumlab URL Configuration

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
from django.urls import path, re_path
from jedzonko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('recipe/list/', recipes),
    path('main/', dashboard),
    re_path(r'^recipe/(?P<id>(\d)+/$)', show_recipe_id),
    path('recipe/add/', add_recipe),
    re_path(r'^recipe/modify/(?P<id>(\d)+/$)', modify_recipe),
    re_path(r'^schedule/(?P<id>(\d)+/$)', schedule_details),
    path('plan/list/', schedules),
    path('plan/add/', add_schedule),
    path('plan/add-recipe/', add_recipe_to_schedule)
]
