from django.shortcuts import render,redirect
from .models import Product, Result, Offer, Requirement, User, Review
from .crawl import GetProductInfo
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        found_user=User.objects.filter(username=request.POST['username'])
        if found_user is not None :
            error='이미 있는 아이디입니다'
            return render(request, 'registration/signup.html',{'error':error})

        new_user =User.objects.create(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('main')

    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        found_user=auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if found_user is not None :
            error='아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html',{'error':error})

        auth.login(
            request, 
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )

        return redirect(request.GET.get('next','/'))

    return render(request, 'registration/login.html')