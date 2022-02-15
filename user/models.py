from django.db import models

class User(models.Model):
    firebase_uid = models.CharField(max_length=28, primary_key=True)
    name = models.CharField(max_length=40)
    latitude = models.FloatField(db_index=True) # 위도 ex): 41.40338
    longitude = models.FloatField(db_index=True) # 경도 ex): 2.17403
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firebase_uid} {self.name}"
