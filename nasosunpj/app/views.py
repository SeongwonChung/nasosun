from django.shortcuts import render,redirect
from .models import Product, Result, Offer, Requirement, User, Review
from .crawl import GetProductInfo
from django.contrib import auth

# Create your views here.


def for_you(request):
    if request.method == "POST":
        
        new_offer = Offer.objects.create(
            user_no = request.user
        )
        new_result = Result.objects.create(
            offer_no = new_offer
        )

        temper_score = request.POST['temperament']
        
        if int(temper_score) > 50:
            temp = "감성적"
        else:
            temp = "실용적"
            
        taste = request.POST['taste']
        print(taste)

        new_requirement = Requirement.objects.create(
            offer_no = new_offer,
            gender =request.POST['gender'],
            age =request.POST['age'],
            taste = taste, 
            temperament =temp,
            purpose =request.POST['purpose'],
            budget =request.POST['budget'],
        )
        return  redirect('result', new_result.pk)
    return render(request, 'for_you.html')

def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['username'])
        if len(found_user) >0 :
            error='이미 있는 아이디입니다'
            return render(request, 'registration/signup.html',{'error':error})

        new_user =User.objects.create(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, 
                    new_user,
                    backend='django.contrib.auth.backends.ModelBackend')
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
import time

def logout(request):
    auth.logout(request)
    return redirect('main')

# Create your views here.
def spinner(request, offer_no):
    requirement = Requirement.objects.get(offer_no = offer_no)
    result = Result.objects.get(offer_no = offer_no)

def result(request, result_pk):
    result = Result.objects.get(offer_no = result_pk)
    requirement = Requirement.objects.get(offer_no = result_pk)

    age = requirement.age
    gender = requirement.gender
    budget = requirement.budget
   
    cnt = 0
    while cnt < 3:
        product = GetProductInfo(age, gender, budget)
        found_product = Product.objects.filter(result_no = result, name=product['name'])
        if len(found_product) == 0:
            new_product = Product.objects.create(
                name = product['name'],
                img_url = product['img_url'],
                price = product['price'],
                product_url = product['product_url'],
                result_no = result
            )
            cnt+=1
        
    products = list(result.products.all().values())[0:3]

    return render(request, 'result.html', {'requirement' : requirement, 'products': products,})


def main(request):
    return render(request, 'main.html')

def membership_suggestion(request):
    return render(request, 'membership_suggestion.html')



