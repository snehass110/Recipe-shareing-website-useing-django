from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
#
# class itemmodel(models.Model):
#     name=models.CharField(max_length=20)
#     ingree=models.CharField(max_length=1100)
#     step=models.CharField(max_length=3000)
#     image=models.ImageField(upload_to="rsapp/static")
# rsapp/models.py



class itemmodel(models.Model):
    email=models.EmailField()
    name = models.CharField(max_length=20)
    type= models.CharField(max_length=20)
    ingree = models.CharField(max_length=2000)
    step = models.CharField(max_length=3000)
    image = models.ImageField(upload_to="rsapp/static")


# class RecipeReview(models.Model):
#     recipe_name = models.CharField(max_length=255)
#     comment = models.TextField()
#     rate = models.IntegerField()



class review_model(models.Model):
    ids=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    comment=models.CharField(max_length=50)
    rate=models.IntegerField()
