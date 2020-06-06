from django.shortcuts import render,redirect
from .models import Product, Result, Offer, Requirement, User, Review
from .crawl import GetProductInfo
# Create your views here.
def main(request):
    return render(request, 'main.html')