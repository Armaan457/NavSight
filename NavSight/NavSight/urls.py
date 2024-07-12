"""
URL configuration for NavSight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user.views import yolo, blip, voice_control
from helper.views import members, number, home, id, log_signup, login, signup, uniqueid1, uniqueid2, navigatorhome, location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yolo/',yolo,name='yolo'),
    path('blip/',blip,name='blip'),
    path('voice_control/',voice_control,name='voice_control'),
    path('', members, name='members'),
    path("words" , number, name="number"),
    path('home/',home,name="home"),
    path('unique_id' , id,name="id"),
    path('log_signup/', log_signup, name='log_signup'),
    path('login', login, name="login"),
    path('signup', signup, name='signup'),
    path('uniqueid1',uniqueid1 , name="uniqueid1"),
    path('uniqueid2' , uniqueid2 , name="uniqueid2"),
    path('navigatorhome' , navigatorhome , name="navigatorhome"),
    path('location', location ,name="location"),
]
