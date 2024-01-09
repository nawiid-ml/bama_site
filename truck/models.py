from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Sell_Truck(models.Model):
    """
    Model representing a car sold by the dealer. 
    """
    brand=models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.IntegerField()
    operation=models.CharField(max_length=250)
    color = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(null=False)
    city = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sell_truck')
    def __str__(self):
        return f"{self.brand}"
    
    class Meta:
        verbose_name = "Sell Truck"


class Truck(models.Model):
    search = models.ForeignKey(Sell_Truck,on_delete=models.CASCADE)        