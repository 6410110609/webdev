from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank = True,default = "/images/placeholder.png",upload_to="images/")
    category = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    rating = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    numReviews = models.IntegerField(null=True,blank=True,default=0)
    price = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    countInStock = models.IntegerField(null=True,blank=True,default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name +" | "+self.category +" | " + str(self.price)


class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    rating =  models.IntegerField(null=True,blank=True,default=0)
    comment = models.TextField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id =  models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.user) + ' | Review ' + str(self.rating) + ' STAR |'


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    paymentMethod = models.CharField(max_length=200,null=True,blank=True)
    taxPrice = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    totalPrice = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    slip = models.ImageField(upload_to="slip/")
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False,null=True, blank=True)
    isConfirm = models.BooleanField(default=False)
    confirmAt = models.DateTimeField(auto_now_add=False,null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    _id =  models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order  = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    qty = models.IntegerField(null=True,blank=True,default=0)
    price = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    image = models.CharField(max_length=200,null=True,blank=True)
    _id =  models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)



class BookingDetails(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
    namebook = models.CharField(max_length=200,null=True,blank=True)
    tel  = models.CharField(max_length=200,null=True,blank=True)
    bdate = models.CharField(max_length=200,null=True,blank=True)
    bookgo = models.CharField(max_length=200,null=True,blank=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.namebook)

