from django.urls import path
from authtoken_example import views

urlpatterns = [
    path("login", views.LoginView.as_view()),
    path("logout", views.LogOutView.as_view())
]
