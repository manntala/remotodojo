from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

def registration_view(request):
    form = RegistrationForm()
    
    if request.method == "POST":
            form = RegistrationForm(request.POST)
    
            if form.is_valid():
                user = form.save(commit=False)
    
                user.is_valid = False
                user.save()
                messages.success(request, "Successfully registered!")
                return redirect(to='/account/login#login')
            else:
                messages.info(request, 'invalid registration details!')
                

    return render(
        request, "account/register.html",
        {"form": form}
    )


    
def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect(account_view)
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)              
                return redirect('dashboard') 
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard')
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
         form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
         )
    context['account_form'] = form
    return render(request, 'account/account.html', context)

class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = 'coreapp/dashboard.html'
    template_name = 'account/account.html'

