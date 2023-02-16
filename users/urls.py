from django.urls import path
from users import views

urlpatterns = [
    path("users/signup/", views.UserCreateView.as_view()),
    path("users/login/", views.UserLoginView.as_view()),
]
