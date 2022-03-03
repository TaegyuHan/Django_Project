from django.urls import path, include
from .views import (
    UserJoinAPIView, UserDeleteAPIView
)

urlpatterns = [
    path("join", UserJoinAPIView.as_view()),
    path("delete", UserDeleteAPIView.as_view()),
    path("login", UserJoinAPIView.as_view()),
]