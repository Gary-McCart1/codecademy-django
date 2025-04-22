from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    price_per_unit = models.FloatField()

class MenuItem(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)