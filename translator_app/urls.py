from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views


app_name = 'translator_app'


urlpatterns = [
    path('',views.translator,name='trnaslator'),
    path('translated/',views.translated,name='translated'),
    path('home',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('profile/',views.profile,name='profile'),
]
