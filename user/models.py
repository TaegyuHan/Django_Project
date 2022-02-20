from django.db import models

class User(models.Model):
    firebase_uid = models.CharField(max_length=28, primary_key=True)
    google_id = models.EmailField()
    google_profile_image = models.CharField(max_length=100)
    google_name = models.CharField(max_length=100)
    app_name = models.CharField(max_length=40)
    latitude = models.FloatField(db_index=True) # 위도 ex): 41.40338
    longitude = models.FloatField(db_index=True) # 경도 ex): 2.17403
    address = models.CharField(max_length=100, default="82, Eunbong-ro, Namdong-gu, Incheon, Republic of Korea")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firebase_uid
