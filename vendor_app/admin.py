from django.contrib import admin

# Register your models here.
from django.contrib import admin
from vendor_app.models import *

class VendorAdmin(admin.ModelAdmin):
	list_display = ['id','first_name', 'last_name', 'phone', 'address', 'zipcode', 'gender', 'store_created', 'verified', 'doc_submitted', 'is_active','is_AVPL_Vendor']
    
class StoreAdmin(admin.ModelAdmin):
	list_display = ['created_at', 'id', 'vendor', 'name', 'registration_number', 'closing_day', 'opening_time', 'closing_time']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'bar_code', 'created_at', 'id', 'store', 'category', 'subcategory', 'subsubcategory', 'brand',  'price', 'stock', 'weight', 'is_active']
	list_editable= ( 'is_active',)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Store, StoreAdmin)



admin.site.register(VendorDocs)
admin.site.register(StoreImages)
admin.site.register(ProductImages)
admin.site.register(ProductVariant
)

admin.site.register(Product, ProductAdmin)
admin.site.register(BusinessLimit)
admin.site.register(BusinessLimitTransaction)
admin.site.register(Recharge_Receipt)
admin.site.register(UserSubscriptionRequest)

admin.site.register(VendorWithdrawRequest)
admin.site.register(ProductRating)
admin.site.register(Vendor_Wallet_Commission)
admin.site.register(VendorWalletTransaction)