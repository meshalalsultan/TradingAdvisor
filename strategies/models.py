from django.db import models

# Create your models here.

# strategies/models.py


class Strategy(models.Model):
    EXPERIENCE_LEVEL = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]

    RISK_LEVEL = [
        ('low', 'Low Risk'),
        ('medium', 'Medium Risk'),
        ('high', 'High Risk'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    experience_level = models.CharField(max_length=15, choices=EXPERIENCE_LEVEL)
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL)
    trading_style = models.CharField(max_length=50, blank=True)  # مثل المضاربة أو التداول اليومي
    analysis_type = models.CharField(max_length=50)  # مثل التحليل الفني أو الأساسي
    psychology = models.CharField(max_length=50, blank=True)  # مثل تفادي المخاطرة، المخاطرة العالية

    def __str__(self):
        return self.name

