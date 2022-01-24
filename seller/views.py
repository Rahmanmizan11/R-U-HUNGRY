from django.shortcuts import render, redirect
from django.contrib import messages
from seller.forms import MenuForm, RestaurantForm
from seller.models import Menu, Restaurant
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_restaurant(request):
    if request.user.userdetail.is_seller:
        return redirect('dashboardProfile')
    form = RestaurantForm()
    context = {
        "form" : form
    }
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.user.userdetail.has_applied = True
            request.user.userdetail.save()
            messages.success(request, 'Restaurant Created Successfully.')
            return redirect('allpyForResturent')
        else:
            messages.success(request, 'Something Wrong!')
    return render(request, 'dashboard/seller/applySeller.html', context)

@login_required
def menuPage(request):
    form = MenuForm()
    id = Restaurant.objects.get(user=request.user).id
    context = {
        "form" : form,
        "rid" : id,
        "menues" : Menu.objects.filter(retaurant_id=id)
    }
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Item addedd successfully!')
            return redirect('menuPage')
        else:
            print(form.errors)
    return render(request, 'dashboard/seller/menu.html', context)


def manage_orders(request):
    pass