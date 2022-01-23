from user_management.models import UserDetail
from django.contrib.auth.models import User
from user_management.forms import ChangePassword, EditUserDetailForm, EditUserForm, UserRegistraionForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    regForm = UserRegistraionForm()
    if request.method == 'POST':
        regForm = UserRegistraionForm(request.POST)
        if regForm.is_valid():
            user = regForm.save()
            new_user = authenticate(username=regForm.cleaned_data.get('username'), password=regForm.cleaned_data.get('password1'))
            login(request,new_user)
            messages.success(request, 'Account Created Successfully.')
            return redirect('user-dashboard')

    dict = {'regForm': regForm}
    return render(request, template_name='user/register.html', context=dict)

def loginPage(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        uName = request.POST.get('user_name')
        pas = request.POST.get('password')
        user = authenticate(request, username=uName, password=pas)
        if user is not None:
            login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('search')
        else:
            messages.error(request, 'Username OR Password is Incorrect')

    return render(request, template_name='user/login.html')

def logoutUser(request):
    logout(request)
    return redirect('search')

@login_required
def userDashboardProfile(request):
    try:
        userDetails = request.user.userdetail
    except:
        userDetails = UserDetail.objects.create(user= request.user)
    
    updateInfoForm = EditUserForm(initial={'uid':request.user.id, 'username': request.user, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})
    updateUserDetailForm = EditUserDetailForm(initial={'contact_no': request.user.userdetail.contact_no, 'address': request.user.userdetail.address})
    cpForm = ChangePassword(request.user)

    dict = {
        'form': updateInfoForm, 
        'cpForm': cpForm, 
        'userDetails': userDetails, 
    }

    if request.method == 'POST':
        if 'btnform1' in request.POST:
            updateInfoForm = EditUserForm(request.POST, instance=request.user)
            updateUserDetailForm = EditUserDetailForm(request.POST, instance=request.user.userdetail)
            
            if updateInfoForm.is_valid() and updateUserDetailForm.is_valid():
                updateInfoForm.save()
                updateUserDetailForm.save()
                messages.success(request, 'Profile Updated Successfully')
                return redirect('user-dashboard')
            else:
                dict['form'] = updateInfoForm


        if 'btnform2' in request.POST:
            cpForm = ChangePassword(request.user, request.POST)

            if cpForm.is_valid():
                user = cpForm.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password Changed Successfully')
                return redirect('user-dashboard')
            else:
                dict['cpForm'] = cpForm

        if 'btnform4' in request.POST:
            dUserID =  request.user.id
            logout(request)
            User.objects.get(id=dUserID).delete()
            return JsonResponse({'status': 200})
    return render(request, template_name='dashboard/profile.html', context=dict)    
