from django.urls import path, include
from .views import (
    UserJoinAPIView, UserDeleteAPIView,
    UserLoginAPIView
)

urlpatterns = [
    path("join", UserJoinAPIView.as_view()),
    path("delete", UserDeleteAPIView.as_view()),
    path("login", UserLoginAPIView.as_view()),
]