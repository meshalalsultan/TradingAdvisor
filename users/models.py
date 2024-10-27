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
    MARKET_ANALYSIS_CHOICES = [
        ('technical', 'Technical Analysis'),
        ('fundamental', 'Fundamental Analysis'),
        ('mixed', 'Mixed Analysis'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    trading_style = models.CharField(max_length=50, blank=True)
    risk_preference = models.CharField(max_length=10, choices=RISK_PREFERENCE)
    goals = models.TextField(blank=True)
    
    # الحقول الجديدة
    preferred_assets = models.TextField(blank=True, help_text="مثل الفوركس، الأسهم، أو العملات الرقمية")
    financial_goals = models.TextField(blank=True, help_text="هدف الربح اليومي، الأسبوعي، أو الشهري")
    trading_hours = models.CharField(max_length=50, blank=True, help_text="ساعات التداول المفضلة")
    market_analysis_preference = models.CharField(max_length=20, choices=MARKET_ANALYSIS_CHOICES, blank=True)

    def recommend_strategies(self):
        strategies = Strategy.objects.filter(
            experience_level=self.experience_level,
            risk_level=self.risk_preference,
            trading_style=self.trading_style
        )
        return strategies

    def __str__(self):
        return f"{self.user.username} - {self.experience_level}"
