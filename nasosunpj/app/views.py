from django.shortcuts import render,redirect
from .models import Product, Result, Offer, Requirement, User, Review
from .crawl import GetProductInfo
import time

# Create your views here.
def spinner(request, offer_no):
    requirement = Requirement.objects.get(offer_no = offer_no)
    result = Result.objects.get(offer_no = offer_no)

    age = requirement.age
    gender = requirement.gender
    budget = requirement.budget

    result_pk = result.pk
    
    for i in range(3):
        product = GetProductInfo(age, gender, budget)
        new_product = Product.objects.create(
            name = product['name'],
            img_url = product['img_url'],
            price = product['price'],
            product_url = product['product_url'],
            result_no = result
        )
        

    return redirect('result', result_pk)

def result(request, result_pk):
    result = Result.objects.get(offer_no = result_pk)
    requirement = Requirement.objects.get(offer_no = result_pk)
    products = result.products.all()

    return render(request, 'result.html', {'requirement' : requirement, 'products': products})


def main(request):
    return render(request, 'main.html')
