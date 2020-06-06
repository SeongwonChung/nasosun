from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    product_url = models.TextField()
    img_url = models.TextField()
    
    def __str__(self):
        return self.name

class Offer(models.Model):
    user_no = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "offers")


class Result(models.Model):
    offer_no = models.OneToOneField(Offer, on_delete = models.CASCADE, primary_key = True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.pk) + "/"+ str(self.offer_no)

class Requirement(models.Model):
    GENDER = (
        ('남자','남자'),
        ('여자','여자')
    )

    TASTE = (
        ('실용','실용적'),
        ('고급','고급스러운')
    )

    TEMPERAMENT = (
        ('외향적','외향적'),
        ('내향적','내향적')
    )
    offer_no = models.OneToOneField(Offer, on_delete = models.CASCADE, primary_key = True)
    gender = models.CharField(max_length = 2, choices = GENDER)
    age = models.IntegerField()
    taste = models.CharField(max_length = 2, choices = TASTE) #취향
    temperament = models.CharField(max_length = 3, choices = TEMPERAMENT) #성향
    purpose = models.CharField(max_length = 100)
    budget = models.IntegerField()

    def __str__(self):
            return str(self.pk) + "/"+ str(self.offer_no)

class Review(models.Model):
    offer_no = models.OneToOneField(Offer, on_delete = models.CASCADE, primary_key = True)
    satisfy = models.IntegerField()

    def __str__(self):
        return self.offer_no
