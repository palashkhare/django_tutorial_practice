from django.conf.urls import url
from . import views
# -*- coding: utf-8 -*-

app_name = 'login_app'

urlpatterns = [
            url('contact_me', views.vw_contact_me, name= 'contact_me'),
            url('login', views.vw_login, name= 'user_login'),
            url('logout', views.vw_logout, name= 'logout'),
            url('special', views.special, name= 'special'),
            url('register', views.userRegistration, name= 'register'),
        ]