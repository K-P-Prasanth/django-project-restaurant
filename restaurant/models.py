from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    def __str__(self):
        return f"{self.id} : {self.username}"

class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.id} : {self.name}"

class Item(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    vegBool = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MaxValueValidator(5)])
    imageURL = models.URLField(blank=True)
    category = models.ForeignKey(Category, blank=True,null=True ,on_delete=models.CASCADE, related_name="cat")
    
    def __str__(self):
        return f"{self.id} : {self.name} : {self.rating}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "prices": self.price,
            "vegBool": self.vegBool,
            "rating": self.rating,
            "imageURL": self.imageURL,
            "category_id": self.category.id,
            "category":self.category.name
        }
    

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="sales")
    quantity = models.IntegerField(default=0,validators=[MaxValueValidator(10)])

    def __str__(self):
        return f"User : {self.user} Item : {self.item.name} : {self.quantity}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(Sale,blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} : {self.user.username} : {self.total}"

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "item_ids": [item.item.id for item in self.items.all()],
            "items": [item.item.name for item in self.items.all()],
            # "prices": [item.item.price for item in self.items.all()],
            "quantity": [item.quantity for item in self.items.all()],
            "total": self.total,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }
