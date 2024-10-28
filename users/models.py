from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_level = models.CharField(
        max_length=20,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]
    )
    trading_style = models.CharField(
        max_length=20,
        choices=[('day trading', 'Day Trading'), ('swing trading', 'Swing Trading'), ('long term', 'Long-term Investment')]
    )
    risk_preference = models.DecimalField(max_digits=5, decimal_places=2)  # نسبة المخاطرة كنسبة مئوية
    preferred_assets = models.CharField(max_length=100)
    financial_goals = models.CharField(max_length=100)  # يمكن تخصيص الحقل أكثر إذا لزم
    trading_hours = models.CharField(max_length=50)
    market_analysis_preference = models.CharField(
        max_length=20,
        choices=[('technical', 'Technical'), ('fundamental', 'Fundamental'), ('both', 'Both')]
    )
    strategy = models.TextField(null=True, blank=True)  # لتخزين الاستراتيجية التي تم إنشاؤها بواسطة ChatGPT

    def __str__(self):
        return f"{self.user.username} Profile"
