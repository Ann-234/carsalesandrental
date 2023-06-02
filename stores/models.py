from django.db import models
from users.models import Profile
import secrets
from .paystack import Paystack
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Carousel(models.Model):
    slide = models.ImageField(upload_to='slider')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)


class CarCategory(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='category',null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class CarProduct(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    inventory = models.PositiveIntegerField()
    brand = models.CharField(max_length=225)
    year_Manufacture= models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2023),
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product')
    category=models.ForeignKey(CarCategory,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f' Cart ::::: {str(self.total)}'
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(CarProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Cart id :: {self.cart_id} --- {self.quantity}'



ORDER_STATUS = (
  ('pending','pending'),
  ('cancel payment','cancel payment'),
  ('payment received','payment received'),
  ('order in progress','order in progress'),
  ('order received','order received')

)
PAYMENT_METHOD =(
  ('Paystack','Paystack'),
  ('Transfer','Transfer')
)   
 

class  Order(models.Model):
   cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
   order_by = models.CharField(max_length=225)
   shipping_address = models.TextField()
   mobile = models.CharField(max_length=50)
   email=models.EmailField(max_length=50)
   discount = models.PositiveIntegerField()
   subtotal = models.PositiveIntegerField()
   amount = models.PositiveIntegerField()
   created_at = models.DateField(auto_now_add=True)
   order_status = models.CharField(max_length=255,choices=ORDER_STATUS,default='pending')
   payment_method = models.CharField(max_length=255,choices=PAYMENT_METHOD,default='Paystack')
   payment_complete = models.BooleanField(default=False)
   ref = models.CharField(max_length=255,null=True,blank=True)
  
   def __str__(self):
      return f'{self.order_status} ::: {self.id}'
  

    # ref generate
   def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            obj_with_sm_ref = Order.objects.filter(ref = ref)
            if not obj_with_sm_ref:
                self.ref = ref
        super().save(*args,**kwargs)


     # amount
   def amount_value(self)-> int:
        return self.amount * 100
    
    # verification
   def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount']/100 == self.amount:
                self.payment_complete = True
                self.payment_method = 'Payment Received'
            self.save()

        if self.payment_complete:
            return True
        return False