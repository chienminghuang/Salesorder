#from django.db import models

# Create your models here.
#class Order (models.Model):
#    name = models.CharField(max_length=200);
#    phone = models.CharField(max_length=20);
#    address = models.TextField();
#    delivery_date = models.DateField(blank=True);
#    product_id = models.TextField();
#    payment_option = models.CharField(max_length=50);
#    amount = models.IntegerField();
#    order_status = models.CharField(max_length=50);


#from django.db.models import ForeignKey
#class 商品類別表(models.Model):
#    名稱 = models.CharField(max_length=50,unique=True)
#    描述 = models.TextField()
#    圖片 = models.ImageField(upload_to='category', blank=True)

#    class Meta:
#        verbose_name_plural = "商品類別表"
#        db_table = '商品類別表'

#   def __str__(self):
#       return self.名稱




#class 產品列表(models.Model):
#    名稱 = models.CharField(max_length=100, unique=True)
#    描述 = models.TextField(blank=True)
#    圖片 = models.ImageField(upload_to='category', blank=True)
#    所屬類別 = models.ForeignKey(商品類別表, on_delete=models.CASCADE)
#    價格 = models.DecimalField(max_digits=10, decimal_places=4)
#    庫存 = models.IntegerField(default=0)
#    已上架 = models.BooleanField(default=True)
#    建立時間 = models.DateTimeField(auto_now_add=True)
#    修改時間 = models.DateTimeField(auto_now_add=True)

    # Meta後台管理介面
#    class Meta:
#        verbose_name_plural = "產品列表"
#        db_table = '產品列表'
#        ordering = ('-建立時間',)
#        def __str__(self):
#            return self.名稱



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Curtain(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(max_length=100)  # Field name made lowercase.
    category = models.CharField(max_length=100, unique=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=45)  # Field name made lowercase.
    #price = models.DecimalField(max_digits=10, decimal_places=4)
    material1 = models.ImageField(upload_to='category', blank=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='Material2', max_length=45)  # Field name made lowercase.
    material3 = models.CharField(db_column='Material3', max_length=45)  # Field name made lowercase.
    #recommend = models.BooleanField(default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curtain'


class Curtaincategory(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurtainCategory'

class Sofa(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(max_length=100)  # Field name made lowercase.
    Width = models.IntegerField(default=0)
    Height = models.IntegerField(default=0)
    model = models.CharField(db_column='Model', max_length=45)  # Field name made lowercase.
    #price = models.DecimalField(max_digits=10, decimal_places=4)
    material1 = models.ImageField(upload_to='category', blank=True)  # Field name made lowercase.
    material2 = models.CharField(db_column='Material2', max_length=45)  # Field name made lowercase.
    material3 = models.CharField(db_column='Material3', max_length=45)  # Field name made lowercase.
    #recommend = models.BooleanField(default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sofa'



class Employee(models.Model):
    employeeid = models.BigIntegerField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee'


class Favorite(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    memberaccount = models.CharField(db_column='MemberAccount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productid = models.BigIntegerField(db_column='ProductId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Favorite'


class Member(models.Model):
    account = models.CharField(db_column='Account', primary_key=True, max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member'


class Memberphoto(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    memberaccount = models.CharField(db_column='MemberAccount', max_length=45)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=45)  # Field name made lowercase.
    productid = models.BigIntegerField(db_column='ProductId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberPhoto'


class Product(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    detailid = models.CharField(db_column='DetailId', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    photo = models.ImageField(upload_to='category', blank=True)  # Field name made lowercase.
    price = models.BigIntegerField(db_column='Price')  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=45)  # Field name made lowercase.
    recommend = models.BooleanField(default=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Product'


class Salesorder(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    memberaccount = models.CharField(db_column='MemberAccount', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    ordertime = models.DateField(db_column='OrderTime')  # Field name made lowercase.
    orderstatus = models.BooleanField(default=True)  # Field name made lowercase.
    paymentstatus = models.BooleanField(default=True)  # Field name made lowercase..
    productid = models.BigIntegerField(db_column='ProductId')  # Field name made lowercase.
    Width = models.IntegerField(default=0)
    Height = models.IntegerField(default=0)
    Estimate = models.IntegerField(default=0)
    photo1 = models.ImageField(upload_to='category', blank=True)  # Field name made lowercase.
    photo2 = models.CharField(db_column='Photo2', max_length=45)  # Field name made lowercase.
    photo3 = models.CharField(db_column='Photo3', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesOrder'


class Shoppingcart(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    memberaccount = models.CharField(db_column='MemberAccount', max_length=45)  # Field name made lowercase.
    memberphotoid = models.BigIntegerField(db_column='MemberPhotoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShoppingCart'


class Wallpaper(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.
    category = models.BigIntegerField(db_column='Category')  # Field name made lowercase.
    recommend = models.IntegerField(db_column='Recommend')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wallpaper'


class Wallpapercategory(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WallpaperCategory'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


#class AuthGroupPermissions(models.Model):
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#    class Meta:
#        db_table = 'auth_group_permissions'
#        unique_together = (('group', 'permission'),)
