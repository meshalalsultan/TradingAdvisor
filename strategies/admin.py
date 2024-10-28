from django.contrib import admin

def register_models():
    from .models import TradingStrategy  # استيراد النموذج داخل الدالة
    admin.site.register(TradingStrategy)

register_models()
