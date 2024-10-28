from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Recommendation(models.Model):
    strategy = models.ForeignKey('strategies.TradingStrategy', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField(default="No recommendation")
    created_at = models.DateTimeField(default=timezone.now)  # تعيين القيمة الافتراضية للتاريخ الحالي

    def __str__(self):
        return f"Recommendation for {self.user.username}"
