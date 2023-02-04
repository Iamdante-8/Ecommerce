from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User,db_column='user_id', on_delete=models.SET_NULL, null=True)
    name = models.CharField(db_column='product_name',max_length=200, null=True, blank=True)
    image =  models.ImageField(db_column='product_image',null=True, blank=True)
    brand = models.CharField(db_column='product_brand',max_length=200, null=True, blank=True)
    category = models.CharField(db_column='product_category',max_length=200, null=True, blank=True)
    description = models.TextField(db_column='product_description',null=True, blank=True)
    rating = models.DecimalField(
        db_column='product_rating',max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(db_column='product_numReviews',null=True, blank=True, default=0)
    price = models.DecimalField(
        db_column='product_price',max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(db_column='product_countInStock',null=True, blank=True, default=0)
    createdAt = models.DateTimeField(db_column='product_createdAt',auto_now_add=True)
    _id = models.AutoField(db_column='product_id',primary_key=True, editable=False)
    class Meta:
        db_table='product'
        ordering=('brand',)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product,db_column='review_product' ,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,db_column='review_user_id' ,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200,db_column='review_name', null=True, blank=True)
    rating = models.IntegerField(db_column='review_rating',null=True, blank=True, default=0)
    comment = models.TextField(db_column='review_comment',null=True, blank=True)
    createdAt = models.DateTimeField(db_column='review_createdAt',auto_now_add=True)
    _id = models.AutoField(db_column='review_id',primary_key=True, editable=False)
    class Meta:
        db_table='review'
        ordering=('rating',)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User,db_column='order_user_id' ,on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(db_column='order-paymentMethod',max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        db_column='order_taxPrice',max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        db_column='order_shippingPrice',max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        db_column='order_totalPrice',max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(db_column='order_isPaid',default=False)
    paidAt = models.DateTimeField(db_column='order_paidAt',auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(db_column='order_isDelivered',default=False)
    deliveredAt = models.DateTimeField(
        db_column='order_deliveredAt',auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(db_column='order_createdAt',auto_now_add=True)
    _id = models.AutoField(db_column='order_id',primary_key=True, editable=False)
    class Meta:
        db_table='order'
        ordering=('-paidAt',)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,db_column='orderItem_productName', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,db_column='orderItem_order',on_delete=models.SET_NULL, null=True)
    name = models.CharField(db_column='orderItem_Name',max_length=200, null=True, blank=True)
    qty = models.IntegerField(db_column='orderItem_qty',null=True, blank=True, default=0)
    price = models.DecimalField(
        db_column='orderItem_price',max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(db_column='orderItem_image',max_length=200, null=True, blank=True)
    _id = models.AutoField(db_column='orderItem_id',primary_key=True, editable=False)
    class Meta:
        db_table='orderitem'
        ordering=('-order',)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order,db_column='shippingAddress_order',on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(db_column='shippingAddress_address',max_length=200, null=True, blank=True)
    city = models.CharField(db_column='shippingAddress_city',max_length=200, null=True, blank=True)
    postalCode = models.CharField(db_column='shippingAddress_postalCode',max_length=200, null=True, blank=True)
    country = models.CharField(db_column='shippingAddress_country',max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        db_column='shippingAddress_shippingPrice',max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(db_column='shippingAddress_id',primary_key=True, editable=False)
    class Meta:
        db_table='shippingAddress'
        ordering=('-order',)

    def __str__(self):
        return str(self.address)