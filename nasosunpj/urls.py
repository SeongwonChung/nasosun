"""nasosunpj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views

urlpatterns = [
    #auth
    path('registration/signup',views.signup, name="signup"),
    path('registration/login',views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),
    path('accounts/',include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('for_you', views.for_you, name="for_you"),
    path('', views.main, name="main"),
    path('spinner/<int:offer_no>', views.spinner, name = "spinner" ),
    path('result/<int:result_pk>', views.result, name="result"),
    path('membership_suggestion/',views.membership_suggestion,name="suggestion"),
]
