from recommendations.models import Recommendation
from django.shortcuts import render
from users.models import UserProfile

def dashboard(request):
    # التحقق من وجود UserProfile للمستخدم
    user = request.user
    if not hasattr(user, 'userprofile'):
        # إنشاء UserProfile جديد للمستخدم إذا لم يكن موجودًا
        user_profile = UserProfile.objects.create(user=user, experience_level='beginner', trading_style='day trading', risk_preference='medium')
    else:
        user_profile = user.userprofile

    # جلب التوصيات للمستخدم
    recommendations = Recommendation.objects.filter(user_profile=user_profile)
    return render (request, 'dashboard.html', {'recommendations': recommendations})
