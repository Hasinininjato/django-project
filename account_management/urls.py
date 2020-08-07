from django.urls import path

from . import views

urlpatterns = [
	path('login', views.app_login, name='login'),
	path('logout', views.app_logout, name='logout'),
]
