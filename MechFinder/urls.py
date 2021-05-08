"""mechcheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mechanic/', include('mechanic.urls')),
    path('customer/', include('customer.urls'), name="customer"),

    path('', views.home, name="home"),
    path('signup', views.signupuser, name="signupuser"),
    # path('customer', views.customer, name="customer"),
    path('login', views.loginuser, name="loginuser"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('edit', views.editProfile, name="editProfile"),
    path('services', views.services, name="services"),
    path('about', views.about, name="about"),
    path('faqs', views.faqs, name="faqs"),
    path('contact', views.contact, name="contact"),
    path('feedback', views.feedback, name="feedback"),

]
