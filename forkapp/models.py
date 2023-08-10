

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    job = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField (max_length=13, null=True,  blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    vat = models.CharField(max_length=11, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Product(models.Model):
    name = models.CharField('code', max_length=40)
    altproduct = models.TextField('codes', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=40)
    description = models.TextField(max_length=6000, null=True, blank=True)
    description1 = models.TextField(max_length=6000, null=True, blank=True)
    description2 = models.TextField(max_length=6000, null=True, blank=True)
    marked_price = models.FloatField(max_length=10, null=True, blank=True)
    selling_price = models.FloatField(max_length=10, null=True, blank=True)
    return_policy = models.CharField(max_length=6000, null=True, blank=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey('category', verbose_name='categories', on_delete=models.CASCADE,null=True,blank=True)
    car_type = models.ForeignKey('Car_type', verbose_name='Car_types', on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField('image', upload_to="static/products", null=True, blank=True)
    images1 = models.ImageField('image1', upload_to="static/products", null=True, blank=True)
    images2 = models.ImageField('image2', upload_to="static/products", null=True, blank=True)
    images3 = models.ImageField('image3', upload_to="static/products", null=True, blank=True)
    images4 = models.ImageField('image4', upload_to="static/products", null=True, blank=True)
    images5 = models.ImageField('image5', upload_to="static/products", null=True, blank=True)
    images6 = models.ImageField('image6', upload_to="static/products", null=True, blank=True)
    images7 = models.ImageField('image7', upload_to="static/products", null=True, blank=True)
    images8 = models.ImageField('image8', upload_to="static/products", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Make(models.Model):
    name = models.CharField('Makes', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Make'
        verbose_name_plural = 'Makes'

class Model_type(models.Model):
    name = models.CharField('model_types', max_length=100)
    make = models.ForeignKey('Make', verbose_name='Model_types', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'model_type'
        verbose_name_plural = 'model_types'

class Car_type(models.Model):
    name = models.CharField('car_type', max_length=300)
    model_type = models.ForeignKey('Model_type', verbose_name='Model_types', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'car_type'
        verbose_name_plural = 'car_types'

class Category(models.Model):
    name = models.CharField('categories', max_length=100)
    car_type = models.ForeignKey('Car_type', verbose_name='Car_types', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'categories'
        verbose_name_plural = 'categories'

class Cart(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    total = models.FloatField(default=0, max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.FloatField(max_length=10, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    subtotal = models.FloatField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Τραπεζικό έμβασμα", "Τραπεζικό έμβασμα"),
    ("Αντικαταβολή", "Αντικαταβολή"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Αντικαταβολή")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)
        
