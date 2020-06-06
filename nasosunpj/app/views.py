from django.shortcuts import render,redirect
from .models import Product, Result, Offer, Requirement, User, Review
from .crawl import GetProductInfo
# Create your views here.


def for_you(request):
    if request.method == "POST":
         new_offer = Offer.objects.create(
             user_no = request.user.pk
         )
         new_reslut = Result.objects.create(
             offer_no = new_offer.pk
         )
         new_requirement = Requirement.objects.create(
             offer_no = new_offer.pk,
             gender =request.POST['gender'],
             age =request.POST['age'],
             taste =request.POST['taste'],
             temperament =request.POST['temperament'],
             purpose =request.POST['purpose'],
             budget =request.POST['budget'],
         )
         return  redirect('spinner', new_result.offer_no)
    return render(request, 'for_you.html')

def spinner(request, request_pk):
    request = request.objects.get(pk=request_pk)
    return render(request, 'spinner.html')
