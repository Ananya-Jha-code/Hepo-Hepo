"""hepo URL Configuration

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
from home.views import home_view
from signup.views import signup_view
from login.views import login_view, logoutUser
from chatmenu.views import chat_menu, room, checkview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup/', signup_view),
    path('login/', login_view, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('login/chatmenu/', chat_menu, name='chatmenu'),
    path('login/chatmenu/<str:room>/', room, name='room'),
    path('login/chatmenu/checkview', checkview, name='checkview'),

]
