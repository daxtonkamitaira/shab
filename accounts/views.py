from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from .forms import CustomLoginForm, CustomRegisterForm

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm

def registerView(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomRegisterForm()
    return render(request,'registration/register.html',{'form':form})