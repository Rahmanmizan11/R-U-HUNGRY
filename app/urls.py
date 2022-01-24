from django.contrib import admin
from django.urls import path

from user_management import views as userViews
from fooding import views as generalViews 
from seller import views as sellerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication
    path('register/', userViews.register, name='register'),
    path('login/', userViews.loginPage ,name='login'),
    path('logout/',userViews.logoutUser, name='logout'),
    
    # Dashboard 
    path('dashboard/account-info/', userViews.userDashboardProfile, name="user-dashboard"),
    path('dashboard/all-orders/', generalViews.allGeneralOrder, name="allGeneralOrder"),
    path('dashboard/profile/', userViews.profile, name="dashboardProfile"),
    path('dashboard/menu/', sellerViews.menuPage, name="menuPage"),
    path('dashboard/admin/approve/<int:id>/', userViews.approve, name="approve"),
    path('dashboard/admin/reject/<int:id>/', userViews.reject, name="reject"),
    path('dashboard/admin/application-review/', userViews.applicationReview, name="applicationReview"),
    path('dashboard/apply-for-new-resturent/', sellerViews.create_restaurant, name="allpyForResturent"),
    # General menuPage
    path('', generalViews.homePage, name='home'),
   
    path('search/', generalViews.searchPage, name='search'),
]
