"""Educap URL Configuration

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
from django.urls import path,include
import user.views as user_views

urlpatterns = [
    path('', user_views.home,name='home'),
    path('about/',user_views.about,name='about'),
    path('login/', user_views.auth_login, name='auth_login'),
    path('logout/', user_views.auth_logout, name='auth_logout'),
    path('signup/', user_views.signup, name='signup'),
    path('explore/', user_views.explore, name='explore'),
    path('explore_colleges/', user_views.all_colleges, name='all_colleges'),
    path('explore/<courseid>/', user_views.explore_colleges, name='explore_colleges'),
    path('profile/<username>/', user_views.profile, name='profile'),
    path('profile/<username>/consult/', user_views.consult, name='consult'),
    path('profile/<username>/change_password/', user_views.change_password, name='change_password'),
    path('profile/<username>/assessment_test/', user_views.test1, name='test1'),
    path('quiz/<username>/', include('quiz.urls')),
    path('profile/<username>/personality_test/', user_views.test2, name='test2'),
    path('test_result/<username>/', user_views.test_result, name='test_result'),
    path('test_result/<username>/<courseid>/', user_views.colleges, name='colleges'),
    path('profile/<username>/wish/', user_views.wishlist, name='wishlist'),
    path('wishlist/<collegeid>/',user_views.add_wishlist,name='add_wishlist'),
    path('wishlist/remove/<collegeid>/',user_views.remove_wishlist,name='remove_wishlist')
]
