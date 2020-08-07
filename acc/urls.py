from django.urls import path
from .import views

urlpatterns = [
	path('', views.registerpage, name="register"),
	path('login/', views.loginpage, name="login"),
]