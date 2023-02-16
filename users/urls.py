from django.urls import path
from users.views import UserCreateView

urlpatterns = [path("users/signup/", UserCreateView.as_view())]
