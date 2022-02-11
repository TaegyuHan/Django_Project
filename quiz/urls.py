from django.urls import path, include
from .views import helloAPI, random_quiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", random_quiz),
]