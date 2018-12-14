from django.contrib import admin

from .models import Product,Curtain,Sofa,Salesorder
from import_export.admin import ImportExportModelAdmin

# Register your models here.


#admin.site.register(產品列表)

#class 商品類別表Admin(admin.ModelAdmin):
#    list_display = ['id','名稱','圖片']

#admin.site.register(商品類別表,商品類別表Admin)




class  ProductAdmin(admin.ModelAdmin):
    list_display = [ 'detailid','name','photo', 'price', 'material','recommend']
    list_editable = ['name','price','material','recommend'  ]
    list_per_page = 10

admin.site.register(Product,ProductAdmin)

class   CurtainAdmin(admin.ModelAdmin):
    list_display = ['id','description','model']
    list_editable = ['description','model']
admin.site.register(Curtain,CurtainAdmin)

class   SofaAdmin(admin.ModelAdmin):
    list_display = ['id','description','model']
    list_editable = ['description','model']
admin.site.register(Sofa,SofaAdmin)

@admin.register(Salesorder)
class   SalesorderAdmin(ImportExportModelAdmin):
    list_display = ['id','memberaccount','Estimate','Width','Height','orderstatus']
    list_editable = ['orderstatus']
#admin.site.register(Salesorder,SalesorderAdmin)

#class   SalesorderResource(resources.ModelResource):
#    class Meta:
#        model = Salesorder