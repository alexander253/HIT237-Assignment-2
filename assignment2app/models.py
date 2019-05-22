from django.db import models

# Create your models here.
class CasinoModel(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class TableGameModel(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=50) #card, poker, dice, roulette
    min_bet= models.IntegerField()
    max_bet= models.IntegerField()
    floor= models.CharField(max_length=50) #incase ground floor or below, use charfield
    casino = models.ManyToManyField(CasinoModel)

    def __str__(self):
        return self.name

class RestaurantModel(models.Model):
    name = models.CharField(max_length=30)
    theme = models.CharField(max_length=50) #chinese, italian, etc
    opening_time= models.IntegerField()
    closing_time= models.IntegerField()
    casino = models.ManyToManyField(CasinoModel)

    def __str__(self):
        return self.name
