from django.db import models
from user.models import User


class Category(models.Model):
    """ 카테고리 모델 """
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Report(models.Model):
    """ 신고 보고서 """
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="user_report", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="category_report", on_delete=models.CASCADE)
    title = models.TextField() # 제목
    explanation = models.TextField() # 내용
    solved_title = models.TextField(default="") # 해결 완료 제목
    solved_explanation = models.TextField(default="") # 해결 완료 내용
    latitude = models.FloatField(db_index=True) # 위도 ex): 41.40338
    longitude = models.FloatField(db_index=True) # 경도 ex): 2.17403
    recommendation = models.IntegerField() # 추천 수
    solved = models.BooleanField() # 해결 상태

    # solved 정보
    solved_user = models.TextField(default="", max_length=30)
    solved_google_profile_image = models.TextField(default="", max_length=500)
    solved_app_name = models.TextField(default="", max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    solved_created_at = models.DateTimeField(auto_now_add=True)
    solved_updated_at = models.DateTimeField(auto_now=True)

    class Meta: # 추천 수 정렬
        ordering = ['-recommendation']

    def __str__(self):
        return f"ID: {self.id} => {self.title}"


class ReportRecommendation(models.Model):
    """ 신고 보고서 """
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="user_recommendation", on_delete=models.CASCADE)
    report = models.ForeignKey(
        Report, related_name="report_recommendation", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """ 댓글 """
    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    user = models.ForeignKey(
        User, related_name="user_comment", on_delete=models.CASCADE)
    report = models.ForeignKey(
        Report, related_name="report_comment", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # 추천 수 정렬
        ordering = ['-created_at']

def report_name_file(instance, filename):
    return '/'.join(['static/report', str(instance.report_id), filename])


class ReportImage(models.Model):
    """ 보고 이미지 """
    id = models.BigAutoField(primary_key=True)
    report = models.ForeignKey(
        Report, related_name="report_image", on_delete=models.CASCADE)

    image = models.ImageField(upload_to=report_name_file, blank=True, null=True)

    def __str__(self):
        return f"report id : {self.report_id}"


def report_solved_name_file(instance, filename):
    return '/'.join(['static/report_solved', str(instance.report_id), filename])


class ReportSolvedImage(models.Model):
    """ 해결 이미지 """
    id = models.BigAutoField(primary_key=True)
    report = models.ForeignKey(
        Report, related_name="report_solved_image", on_delete=models.CASCADE)

    image = models.ImageField(upload_to=report_solved_name_file, blank=True, null=True)

    def __str__(self):
        return f"report id : {self.report_id}"