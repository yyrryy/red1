from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=150)
    code=models.CharField(max_length=150, default=None, null=True)
    image=models.ImageField(upload_to='categories_images/', blank=True, null=True)
    def __str__(self) -> str:
        return self.name
class Brand(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
class Model(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Mark(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='marks_images/', blank=True, null=True)
    def __str__(self) -> str:
        return self.name



class Produit(models.Model):
    name=models.CharField(max_length=500, null=True)
    #price
    price= models.FloatField(default=0.00)
    sellprice= models.FloatField(default=0.00)
    remise= models.IntegerField(default=0)
    prixnet= models.FloatField(default=0.00)
    checkprice= models.FloatField(default=None, null=True, blank=True)
    equivalent=models.TextField(default=None, null=True, blank=True)
    #stock
    # stock=models.IntegerField(default=1)
    stock=models.BooleanField(default=True)


    #ref
    ref=models.CharField(max_length=50)

    #image
    image=models.ImageField(upload_to='product_images/', blank=True, null=True)
    mark=models.ForeignKey(Mark, on_delete=models.CASCADE, default=None, null=True, blank=True)
    #cartgrise
    # n_chasis=models.CharField(max_length=50, null=True)
    min=models.CharField(max_length=500, default=None, null=True, blank=True)
    isoffer=models.BooleanField(default=False)
    offre=models.CharField(max_length=500, default=None, null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, default=None, null=True, blank=True)
    cars=models.TextField(default="")
    # brand=models.CharField(max_length=25, default=None)
    # model=models.CharField(max_length=25, default=None)
    # mark=models.CharField(max_length=25, default=None)
    def __str__(self) -> str:
        return self.ref
# cupppon codes table
class Coupon(models.Model):
    code = models.CharField(max_length=50)
    amount = models.FloatField()


class Commercial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    name=models.CharField(max_length=200)
    region=models.CharField(max_length=200, null=True, default=None)
    phone=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    represent=models.ForeignKey('Represent', on_delete=models.CASCADE, default=None, null=True, related_name="repclient")
    user = models.OneToOneField(User, on_delete=models.SET_NULL, default=None, null=True)
    moderegl=models.CharField(max_length=200, default=0, null=True, blank=True)
    name=models.CharField(max_length=200)
    clientname=models.CharField(max_length=200, null=True, default=None, blank=True)
    code=models.CharField(max_length=200, null=True, default=None)
    ice=models.CharField(max_length=200, null=True, default=None)
    city=models.CharField(max_length=200, null=True, default=None)
    region=models.CharField(max_length=200, null=True, default=None)
    total=models.FloatField(default=0.00, null=True, blank=True)
    soldtotal=models.FloatField(default=0.00, null=True, blank=True)
    soldbl=models.FloatField(default=0.00, null=True, blank=True)
    soldfacture=models.FloatField(default=0.00, null=True, blank=True)
    address=models.CharField(max_length=200)
    location=models.TextField(default='', null=True, blank=True)
    phone=models.CharField(max_length=200, default=None, null=True)
    phone2=models.CharField(max_length=200, default=None, null=True)
    diver=models.BooleanField(default=False)
    accesscatalog=models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.name+'-'+str(self.city)


class Connectedusers(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    activity=models.CharField(max_length=500, default=None, null=True, blank=True)
    lasttime=models.DateTimeField(auto_now_add=True)


class Represent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    name=models.CharField(max_length=200, default=None)
    region=models.CharField(max_length=200, null=True, default=None)
    phone=models.CharField(max_length=200, default=None)
    def __str__(self) -> str:
        return self.name




# orders table
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    code=models.CharField(max_length=50, null=True, default=None)
    # name will be a string
    # email will be a string and not requuired
    salseman=models.ForeignKey(Represent, on_delete=models.SET_NULL, null=True, default=None)
    modpymnt=models.CharField(max_length=50, null=True, default=None)
    modlvrsn=models.CharField(max_length=50, null=True, default=None)
    total=models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    # totalremise will be there i ncase pymny is cash
    totalremise=models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    isdelivered = models.BooleanField(default=False)
    ispaied = models.BooleanField(default=False)
    clientname=models.CharField(max_length=500, null=True, default=None)
    clientphone=models.CharField(max_length=500, null=True, default=None)
    clientaddress=models.CharField(max_length=500, null=True, default=None)
    client=models.ForeignKey(Client, on_delete=models.CASCADE, default=None, null=True)
    isclient=models.BooleanField(default=False)
    # order by date
    class Meta:
        ordering = ['-date']
    # return the name and phone

    # methode to determine wether it's delivered or not

    def __str__(self) -> str:
        return f'{self.id} {self.client}'


class Orderitem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Produit, on_delete=models.CASCADE, default=None, null=True)
    ref=models.CharField(max_length=100, null=True, default=None)
    name=models.CharField(max_length=100, null=True, default=None)
    qty=models.IntegerField()
    total=models.FloatField(default=0.00, null=True, blank=True)
    date=models.DateTimeField(default=datetime.datetime.now, blank=True)
    offer=models.CharField(max_length=500, default=None, null=True, blank=True)


class Shippingfees(models.Model):
    city=models.CharField(max_length=20)
    shippingfee=models.FloatField()
    def __str__(self) -> str:
        return f'{self.city} - {self.shippingfee}'




class Pairingcode(models.Model):
    code = models.CharField(max_length=50)
    amount = models.FloatField()

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total=models.FloatField()

class Cartitem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Produit, on_delete=models.CASCADE)
    qty=models.IntegerField()
    total=models.FloatField()
    date=models.DateTimeField(default=datetime.datetime.now, blank=True)
    def __str__(self) -> str:
        return f'{self.product} - {self.qty}'