# Generated by Django 4.2.13 on 2024-07-24 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0003_remove_foodnutrient_amount_food_calories_100g_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portion_size', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Foods.food')),
            ],
        ),
    ]
