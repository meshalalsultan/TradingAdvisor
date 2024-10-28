from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from users.models import UserProfile  # التأكد من استخدام الاستيراد الصحيح
from users.forms import UserCreationForm  # تأكد من وجود هذا النموذج للتسجيل
import openai

# جمع بيانات التداول قبل التسجيل
def collect_user_data(request):
    if request.method == 'POST':
        request.session['experience_level'] = request.POST.get('experience_level')
        request.session['trading_style'] = request.POST.get('trading_style')
        request.session['risk_preference'] = request.POST.get('risk_preference')
        request.session['preferred_assets'] = request.POST.get('preferred_assets')
        request.session['financial_goals'] = request.POST.get('financial_goals')
        request.session['trading_hours'] = request.POST.get('trading_hours')
        request.session['market_analysis_preference'] = request.POST.get('market_analysis_preference')
        return redirect('register')
    return render(request, 'users/collect_user_data.html')

# صفحة التسجيل بعد جمع بيانات التداول
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # جلب بيانات التداول من الجلسة
            UserProfile.objects.create(
                user=user,
                experience_level=request.session.get('experience_level'),
                trading_style=request.session.get('trading_style'),
                risk_preference=request.session.get('risk_preference'),
                preferred_assets=request.session.get('preferred_assets'),
                financial_goals=request.session.get('financial_goals'),
                trading_hours=request.session.get('trading_hours'),
                market_analysis_preference=request.session.get('market_analysis_preference')
            )
            return redirect('generate_strategy')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# توليد استراتيجية باستخدام ChatGPT
@login_required
def generate_strategy(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    # إعداد prompt
    prompt = f"""
    Based on the following user data, provide a comprehensive trading strategy:
    Experience Level: {user_profile.experience_level}
    Trading Style: {user_profile.trading_style}
    Risk Management: {user_profile.risk_preference}
    Preferred Assets: {user_profile.preferred_assets}
    Financial Goals: {user_profile.financial_goals}
    Trading Hours: {user_profile.trading_hours}
    Market Analysis Preference: {user_profile.market_analysis_preference}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    strategy_text = response['choices'][0]['message']['content'].strip()

    # حفظ الاستراتيجية
    user_profile.strategy = strategy_text
    user_profile.save()
    
    return redirect('view_strategy')

# عرض الاستراتيجية في لوحة التحكم
@login_required
def view_strategy(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'users/view_strategy.html', {'strategy': user_profile.strategy})
