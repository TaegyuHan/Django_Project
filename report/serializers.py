from rest_framework import serializers
from .models import (
    Category, Comment,
    Report, ReportRecommendation,
    ReportImage, ReportSolvedImage
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ReportRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportRecommendation
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportImage
        fields = '__all__'


class ReportSolvedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSolvedImage
        fields = '__all__'