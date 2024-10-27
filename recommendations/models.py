# recommendations/models.py

from django.db import models
from users.models import UserProfile
from strategies.models import Strategy

class Recommendation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    date_recommended = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    @staticmethod
    def generate_recommendations(user_profile):
        # استخدام دالة التصفية من UserProfile للحصول على الاستراتيجيات المناسبة
        recommended_strategies = user_profile.recommend_strategies()
        recommendations = []
        for strategy in recommended_strategies:
            recommendation, created = Recommendation.objects.get_or_create(
                user_profile=user_profile,
                strategy=strategy
            )
            recommendations.append(recommendation)
        return recommendations
