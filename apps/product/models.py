from django.db import models

from core.models import BaseModel
from apps.users.models import User

class Category(BaseModel):
    name = models.CharField()
    featured_product = models.OneToOneField('Product', on_delete=models.CASCADE, blank=True, null=True, related_name='featured_product')
    slug = models.SlugField(default=None)
    icon = models.CharField(max_length=30, default=None, blank=True, null=True)


class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/img', blank=True, null=True, default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    slug = models.SlugField(default=None)

    def __str__(self) -> str:
        return self.name
    
    @property
    def new_price(self):
        if self.discount:
            new_price = self.price - ((30/100)*self.price)
        else:
            new_price = self.price

        return new_price
    
    @property
    def img(self):
        if self.image == "":
            self.image = ""
        
        return self.image
    

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.id)

    @property
    def num_of_items(self):
        cartitems = self.cartitems_set.all()
        qtysum = sum([qty.quantity for qty in cartitems])
        return qtysum
    
    @property
    def cart_total(self):
        cartitems = self.cartitems_set.all()
        qtysum = sum([ qty.subTotal for qty in cartitems])
        return qtysum


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=0)
    
    
    @property
    def subTotal(self):
        total = self.quantity * self.product.price
        
        return total
    

class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    added = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)