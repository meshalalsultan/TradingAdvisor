"""
URL configuration for TradingAdvisor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views  # تعديل الاستيراد لمطابقة التطبيق الصحيح

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('user_profile/', user_views.collect_user_data, name='collect_user_data'),  # لتجميع بيانات المستخدم
    path('generate_strategy/', user_views.generate_strategy, name='generate_strategy'),  # لإرسال prompt إلى ChatGPT واستقبال الاستراتيجية
    path('view_strategy/', user_views.view_strategy, name='view_strategy'),  # لعرض الاستراتيجية للمستخدم
]
