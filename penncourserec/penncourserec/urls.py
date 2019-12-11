"""penncourserec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core.views import splash, select, recommend, course_view, learn_more, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('select', select, name='select'),
    path('recommend', recommend, name='recommend'),
    path('course', course_view, name='course'),
    path('learnmore', learn_more, name='learnmore'),
    path('about', about, name='about')
]
