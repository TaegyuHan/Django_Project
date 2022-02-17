from django.urls import path, include
from rest_framework import routers

from .views import (
    CategoryAPIView, CategoryDetailAPIView,
    ReportAPIView, ReportDetailAPIView,
    CommentAPIView, CommentDetailAPIView,
    ReportImageviewset, ReportSolvedviewset,
    ReportDetailCommentsAPIView, ReportRecommendationAPIView,
    ReportDetailImageAPIView, ReportDetailSolvedImageAPIView
)

router = routers.DefaultRouter()
router.register(r'upload', ReportImageviewset)
router.register(r'solved_upload', ReportSolvedviewset)

urlpatterns = [
    path("category/", CategoryAPIView.as_view()),
    path("category/<int:id>/", CategoryDetailAPIView.as_view()),

    path("", ReportAPIView.as_view()),
    path("<int:id>/", ReportDetailAPIView.as_view()),

    path("<int:id>/solved_images/", ReportDetailSolvedImageAPIView.as_view()),
    path("<int:id>/images/", ReportDetailImageAPIView.as_view()),
    path("<int:id>/comments/", ReportDetailCommentsAPIView.as_view()),

    path("recommendation/", ReportRecommendationAPIView.as_view()),

    path("comment/", CommentAPIView.as_view()),
    path("comment/<int:id>/", CommentDetailAPIView.as_view()),

    path('images/', include(router.urls)),
]