# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.home, name='home'),

    # The index page
    path('index/', views.index, name='index'),

    path('index/users/', views.users, name="users"),
    # path('index/user_edit/', views.user_edit, name="user_edit"),

    path('testing/', views.testing, name='testing'),
    path('newCustomer/', views.newCustomer, name='newCustomer'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
