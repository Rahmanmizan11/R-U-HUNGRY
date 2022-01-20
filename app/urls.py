from django.contrib import admin
from django.urls import path
from user_management import views as userViews
from fooding import views as generalViews 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication
    path('register/', userViews.register, name='register'),
    path('login/', userViews.loginPage ,name='login'),
    path('logout/',userViews.logoutUser, name='logout'),
    # Dashboard 
    path('dashboard/account-info/', userViews.userDashboardProfile, name="user-dashboard"),
    # General 
    path('', generalViews.homePage, name='home'),
    path('search/', generalViewsgi.searchPage, name='search'),
]
