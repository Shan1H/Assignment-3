from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
admin.py:

from django.contrib import admin

from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)

from pizzas.models import Pizza
Pizza.objects.all()
QuerySet [<Pizza: Hawaiian>, <Pizza: Meat Lovers>]>
pizzas = Pizza.objects.all()
for pizza in pizzas:
    print(pizza.id, pizza)
Hawaiian
Meat Lovers
p = Pizza.objects.get(id=1)
p.name
