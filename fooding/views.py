from seller.models import Menu, Restaurant
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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

def cartPage(request):
    # Can order 
    # can remove from cart 
    return render(request, '')
 
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