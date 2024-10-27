from django.db import models
from django.contrib.auth.models import User
from strategies.models import Strategy  # تأكد من استيراد Strategy

class UserProfile(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    RISK_PREFERENCE = [
        ('low', 'Low Risk'),
        ('medium', 'Medium Risk'),
        ('high', 'High Risk'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    trading_style = models.CharField(max_length=50, blank=True)
    risk_preference = models.CharField(max_length=10, choices=RISK_PREFERENCE)
    goals = models.TextField(blank=True)

    def recommend_strategies(self):
        strategies = Strategy.objects.filter(
            experience_level=self.experience_level,
            risk_level=self.risk_preference,
            trading_style=self.trading_style
        )
        return strategies

    def __str__(self):
        return f"{self.user.username} - {self.experience_level}"
