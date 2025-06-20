from django.shortcuts import render, redirect
from .models import FoodItem
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    today = timezone.localtime().date()
    items = FoodItem.objects.filter(date_added__date=today)
    total_calories = sum(item.calories for item in items)
    return render(request, 'home.html', { 
        'items': items,
        'total': total_calories
    })

@login_required(login_url='login')
def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        FoodItem.objects.create(name=name, calories=int(calories))
    return redirect('home')

@login_required(login_url='login')
def delete_item(request, item_id):
    FoodItem.objects.filter(id=item_id).delete()
    return redirect('home')

@login_required(login_url='login')
def reset_items(request):
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('home')


