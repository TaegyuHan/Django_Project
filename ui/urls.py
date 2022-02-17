from django.urls import path
from .views import NearReportAPIView

urlpatterns = [
    path("main/", NearReportAPIView.as_view()),
]