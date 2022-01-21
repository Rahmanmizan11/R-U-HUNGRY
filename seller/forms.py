from django import forms
from django.contrib.auth.models import User 
from seller.models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name','price', 'is_available',]


class RestaurantForm(forms.ModelForm):
    pass
    # contact_no = forms.CharField()
    # address = forms.Textarea()
    # gender = forms.CharField()
    # dob = forms.DateField()
    # class Meta:
    #     model = User
    #     fields = ['contact_no','address','gender','dob']


