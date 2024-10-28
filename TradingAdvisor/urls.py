from django.urls import path
from . import views

urlpatterns = [
    path('collect_user_data/', views.collect_user_data, name='collect_user_data'),
    path('register/', views.register, name='register'),
    path('generate_strategy/', views.generate_strategy, name='generate_strategy'),
    path('view_strategy/', views.view_strategy, name='view_strategy'),
]