from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, related_name='foods')
    description = models.TextField(blank=True, null=True)
    calories_100g = models.FloatField(default=0)

    def __str__(self):
        return self.name
    

class Nutrient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=50, default='grams')
    
    def __str__(self):
        return self.name
    

class FoodNutrient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_nutrients')
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    amount_100g = models.FloatField(default=0)

    class Meta:
        unique_together = ('food', 'nutrient')

    def __str__(self):
        return f"{self.amount_100g} {self.nutrient.unit} of {self.nutrient.name} in 100g of {self.food.name}"
    