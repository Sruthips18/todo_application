"""
URL configuration for todoapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.RegistrationView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name='sign-in'),
    path('index',views.IndexView.as_view(),name='index'),
    path('todo/<int:pk>/change',views.TodoUpdateView.as_view(),name='todo-update'),
    path('todo/<int:pk>/remove',views.TodoDeleteView.as_view(),name='deletetodo'),
    path('signout',views.SignOutView.as_view(),name='logout'),
    path('api/',include('api.urls')),
]
