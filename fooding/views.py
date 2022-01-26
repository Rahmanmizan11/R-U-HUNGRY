import json
from urllib import parse
from django.contrib import messages
from fooding.models import Cart
from seller.models import Menu, Restaurant
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
# Create your views here.
def homePage(request):
    restaurants = Restaurant.objects.filter(type='restaurant', )[:8]
    homechefs = Restaurant.objects.filter(type='home', )[:8]
    context = {
        'restaurants' : restaurants,
        'homechefs': homechefs,
    }
    # landing page
    return render(request, 'fooding/index.html', context)

def searchPage(request):
    # Search result
    return render(request, '')

def notificationsPage(request):
    # can give review 
    # can see notifications 
    return render(request, '')

@login_required
def cartPage(request):
    context ={
        'items' : Cart.objects.all(),
        'rid' : Cart.objects.all()[0].restaurant.id,
    }
    return render(request, 'fooding/cart.html', context)

@login_required
def deleteCartItem(request, id):
    Cart.objects.get(id=id).delete()
    messages.success(request, "Item Removed from Cart.")
    return redirect('carts')

@login_required
def addToCart(request, rid, iid):
    path = "/restaurants/menu/" + str(rid)
    # print(path)
    try:
        restaurant = Restaurant.objects.get(id=rid)
        item = Menu.objects.get(id=iid)
        for i in Cart.objects.filter(user_id=request.user.id):
            if i.restaurant.name != restaurant.name:
                i.delete()
                Cart.objects.create(restaurant=restaurant, item=item, user_id=request.user.id, quantity=1, total_price=item.price)
                messages.success(request, "Item Added to Cart. Go to cart page to update quantity. Previous items cleared from cart from another restaurant.")
                return redirect(path)
            elif i.restaurant.name == restaurant.name and i.item.name == item.name:
                i.quantity = i.quantity + 1
                i.total_price = i.total_price + i.item.price
                i.save()
                messages.success(request, "Quantity Increased in Cart")
                return redirect(path)

        Cart.objects.create(restaurant=restaurant, item=item, user_id=request.user.id, quantity=1, total_price=item.price)
        messages.success(request, "Item Added to Cart. Go to cart page to update quantity.")
        return redirect(path)
    except:
        return HttpResponse("Invalid Operation")
    
@login_required
def compliteOrder(request):
    if request.method == 'POST':
        
        data = request.POST.get('senddata')
        print(data)
        return JsonResponse({'status':200})
        
 
def reviewPage(request):
    # see all reviews 
    return render(request, 'fooding/review.html') 

def restaurantPage(request):
    restaurants = Restaurant.objects.filter(type='restaurant', )
    homechefs = Restaurant.objects.filter(type='home', )
    context = {
        'restaurants' : restaurants,
        'homechefs': homechefs,
    } 
    return render(request, 'fooding/restaurent.html', context) 

def menuPage(request, id):
    try:
        x = Restaurant.objects.get(id=id)
        restaurant = Menu.objects.filter(retaurant_id=id, is_available=True)
        context = {
            'restaurantInfo' : x,
            'menuInfo' : restaurant
        }    
        return render(request, 'fooding/menu.html', context) 
    except:
        return HttpResponse("Restaurant Not Found")

    

def createGeneralOrder(request):
    return render(request, 'dashboard/generalUser/addOrder.html')

@login_required
def allGeneralOrder(request):
    return render(request, 'dashboard/generalUser/allOrder.html')