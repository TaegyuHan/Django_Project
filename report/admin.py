from django.contrib import admin
from .models import (
    Category, Report,
    ReportRecommendation, Comment,
    ReportImage, ReportSolvedImage
)

admin.site.register(Category)
admin.site.register(Report)
admin.site.register(ReportRecommendation)
admin.site.register(Comment)
admin.site.register(ReportImage)
admin.site.register(ReportSolvedImage)