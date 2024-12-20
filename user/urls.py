from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/',views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),
    path('user-profile/', views.profile, name='user-profile'),
    path('about-us/', views.aboutus, name='aboutus'),
]