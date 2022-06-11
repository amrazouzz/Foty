
from cProfile import label
import re
from tkinter import Widget
from tokenize import group
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateNewUser, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user
from django.contrib.auth.models import Group


@unauthenticated_user
def login_view(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username = username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.info(request,'اسم المستخدم او كلمة المرور غير صحيحة')
            
    return render(request,"../templates/login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = 'users')
            user.groups.add(group)
            messages.success(request,'تم انشاء الحساب بنجاح')
            return redirect('login')
        
    context={'form':form}
    return render(request,"../templates/register.html",context)
