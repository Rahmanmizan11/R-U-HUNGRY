from django.shortcuts import render

# Create your views here.
def homePage(request):
    # landing page
    return render(request, 'fooding/index.html')

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
    return render(request, '') 

def menuPage(request):
    # can add to cart 
    return render(request, '') 