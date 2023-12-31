from django.db import models

class Motorcycle(models.Model):
    search=models.CharField(max_length=250)
    brand=models.CharField(max_length=250)
    city=models.CharField(max_length=250)


class Sell_Motorcycle(models.Model):
    brand=models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.IntegerField()
    operation=models.CharField(max_length=250)
    color=models.CharField(max_length=100,null=True,blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(null=False)
    city=models.CharField(max_length=250)
    description=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.brand}"
    
    class Meta:
        verbose_name = "Sell Motorcycle"


class   Motorcycle_Price(models.Model):
    model=models.CharField(max_length=250)
    brand=models.CharField(max_length=250)
    Price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField(auto_now_add=True)

