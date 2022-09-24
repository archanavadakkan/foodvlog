from django.urls import path
from . import views

urlpatterns=[
    path('register',views.signup,name='register'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logout,name='logout')
]