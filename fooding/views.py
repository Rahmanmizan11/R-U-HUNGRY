from seller.models import Menu, Restaurant
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
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
     
    return render(request, 'fooding/cart.html')
@login_required
def addToCart(request, rid, iid):
    
    return HttpResponseRedirect(reverse('menuPage1'))
    # return redirect('carts')
 
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