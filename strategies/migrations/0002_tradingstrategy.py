# Generated by Django 5.1.2 on 2024-10-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradingStrategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
