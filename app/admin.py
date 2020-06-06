from django.contrib import admin
from .models import Product, Result, User, Requirement, Review, Offer
# Register your models here.
admin.site.register(Product)
admin.site.register(Result)
admin.site.register(Requirement)
admin.site.register(Review)
admin.site.register(Offer)
