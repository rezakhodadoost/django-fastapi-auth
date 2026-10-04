from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.LoginView.as_view()),
    path("profile/",views.PofileView.as_view()),
    path("register/", views.registerview.as_view())
]