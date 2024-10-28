from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from strategies.models import TradingStrategy
import openai  # تأكد من إعداد مكتبة OpenAI ومفتاح API في الإعدادات

@login_required
def dashboard(request):
    # جلب بيانات المستخدم وآخر استراتيجية
    user_profile = UserProfile.objects.get(user=request.user)
    strategy = TradingStrategy.objects.filter(user=request.user).last()  # الحصول على آخر استراتيجية للمستخدم
    # تمرير البيانات إلى القالب
    return render(request, 'users/dashboard.html', {'user_profile': user_profile, 'strategy': strategy})

@login_required
def collect_user_data(request):
    user = request.user
    if request.method == 'POST':
        # تحديث بيانات UserProfile للمستخدم بعد التسجيل
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.experience_level = request.POST.get('experience_level', 'beginner')
        user_profile.trading_style = request.POST.get('trading_style', 'day trading')
        user_profile.risk_preference = request.POST.get('risk_preference', 'medium')
        user_profile.preferred_assets = request.POST.get('preferred_assets', '')
        user_profile.financial_goals = request.POST.get('financial_goals', '')
        user_profile.trading_hours = request.POST.get('trading_hours', '')
        user_profile.market_analysis_preference = request.POST.get('market_analysis_preference', 'technical')
        user_profile.save()
        
        return redirect('generate_strategy')
    return render(request, 'users/collect_user_data.html')

@login_required
def generate_strategy(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    
    # تكوين prompt باستخدام بيانات المستخدم
    prompt = f"""
    Based on the following information, provide a comprehensive trading strategy:
    Experience Level: {user_profile.experience_level}
    Trading Style: {user_profile.trading_style}
    Risk Management: {user_profile.risk_preference}
    Preferred Assets: {user_profile.preferred_assets}
    Financial Goals: {user_profile.financial_goals}
    Trading Hours: {user_profile.trading_hours}
    Market Analysis Preference: {user_profile.market_analysis_preference}
    """
    
    # الاتصال بـ ChatGPT API للحصول على الاستراتيجية
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    strategy_text = response['choices'][0]['message']['content'].strip()

    # تخزين الاستراتيجية في قاعدة البيانات
    TradingStrategy.objects.create(user=user, strategy_text=strategy_text)

    return redirect('view_strategy')

@login_required
def view_strategy(request):
    strategy = TradingStrategy.objects.filter(user=request.user).last()  # عرض آخر استراتيجية
    return render(request, 'users/view_strategy.html', {'strategy': strategy})
