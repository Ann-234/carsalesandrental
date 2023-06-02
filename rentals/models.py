from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import Profile
import datetime



#create your models here
class Car(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='car')
    brand = models.CharField(max_length=50)
    inventory = models.PositiveIntegerField()
    year_Manufacture = models.IntegerField()
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    CATEGORY={
        ('New','New'),
        ('Used','Used'),
    }
    category = models.CharField(max_length=50,choices=CATEGORY)
    created_at = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title
    

class CarRental(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    start_date=models.DateField()
    end_date=models.DateField()
    total_cost=models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True,null=True)


    def save(self, *args, **kwargs):
        num_days = (self.end_date - self.start_date).days
        self.total_cost = self.car.daily_rate * num_days
        super().save(*args, **kwargs)
    

    def __str__(self):
        return str(self.customer)



    