from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Offer(models.Model):
    user_no = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "offers")

class Result(models.Model):
    offer_no = models.OneToOneField(Offer, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return str(self.pk) + "/"+ str(self.offer_no)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    product_url = models.TextField()
    img_url = models.TextField()
    result_no = models.ForeignKey(Result, on_delete = models.CASCADE, related_name = "products")

    def __str__(self):
        return self.name

class Requirement(models.Model):
    GENDER = (
        ('남자','남자'),
        ('여자','여자')
    )

    offer_no = models.OneToOneField(Offer, on_delete = models.CASCADE, primary_key = True)
    gender = models.CharField(max_length = 2, choices = GENDER)
    age = models.IntegerField()
    taste = models.CharField(max_length = 10) #성향
    temperament = models.CharField(max_length = 10) #취향
    purpose = models.CharField(max_length = 100)
    budget = models.IntegerField()

    def __str__(self):
            return str(self.pk) + "/"+ str(self.offer_no)

class Review(models.Model):
    offer_no = models.OneToOneField(Offer, on_delete = models.CASCADE, primary_key = True)
    satisfy = models.IntegerField()

    def __str__(self):
        return self.offer_no
