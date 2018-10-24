from django.contrib import admin
from .models import Product
# Register your models here.


#admin.site.register(產品列表)

#class 商品類別表Admin(admin.ModelAdmin):
#    list_display = ['id','名稱','圖片']

#admin.site.register(商品類別表,商品類別表Admin)




class  ProductAdmin(admin.ModelAdmin):
    list_display = [ 'detailid','name','photo', 'price', 'material']
    list_editable = ['name','price','material'  ]
    list_per_page = 10

admin.site.register(Product,ProductAdmin)