"""stackoverflow URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomePage, name ='home-page'),
    path('ask-new-question/',views.NewQuestionPage,name='new_question'),
    path('login/',views.LoginPage,name='login'),
    path('login-user',views.UserLogin,name='user-login'),
    path('create-new-question/',views.CreateNewQuestion,name='create-question'),
    path('user-logout/',views.UserLogout,name='user-logout'),
    path('question/',views.QuestionPage,name='question')
]
