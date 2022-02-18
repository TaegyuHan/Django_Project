from django.urls import path
from .views import (
    NearReportAPIView, NearReportListAPIView,
    NearSolvedReportListAPIView
)

urlpatterns = [
    path("main/", NearReportAPIView.as_view()),
    path("report_list/", NearReportListAPIView.as_view()),
    path("solved_report_list/", NearSolvedReportListAPIView.as_view()),
]