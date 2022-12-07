from django.urls import path
from quiz import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('accounts/login/', views.login_page, name="login_page"),
]
