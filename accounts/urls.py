from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('login',views.login, name='login'),
	path('signup',views.signup, name='signup'),
	path('logout',views.logout, name='logout'),
	path('', include('social_django.urls', namespace='social')),
	path('base', views.base, name="base"),
	path('del/<int:item_id>', views.remove, name="del"),
	
]
