from django.shortcuts import render
from .models import Meals, Category


def meal_list(request):
    categories = Category.objects.all()
    meal_list = Meals.objects.all()
    contex = {'meal_list': meal_list,
              "categories": categories,}
    return render(request, 'Meals/list.html', contex)


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)
    contex = {'meal_detail': meal_detail}
    return render(request, 'Meals/detail.html', contex)
2