from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from admin_app.models import *
from main_app.models import *
from .models import *
from main_app.models import *
import datetime
from ckeditor.fields import RichTextField

# Per Product Commission 

class Vendor_Wallet_Commission(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	current_balance = models.FloatField(default=0.0)
	is_active = models.BooleanField(default=False)
	
	def __str__(self):
		return 'Wallet of '+self.user.email

class VendorWalletTransaction(models.Model):
	vendor_wallet_commission = models.ForeignKey(Vendor_Wallet_Commission, on_delete=models.CASCADE)
	transaction_date = models.DateTimeField()
	transaction_type = models.CharField(max_length=20)
	transaction_amount = models.FloatField()
	user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank= True)
	previous_amount = models.FloatField()
	remaining_amount = models.FloatField()
	
	def __str__(self):
		return 'Wallet Transaction ID '+str(self.id)

class Vendor(models.Model):
	user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='vendor')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=20)
	latitude = models.FloatField()
	longitude = models.FloatField()
	gender = models.CharField(max_length=20)
	store_created = models.BooleanField(default=False)
	verified = models.BooleanField(default=False)
	doc_submitted = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_AVPL_Vendor = models.BooleanField(default=False)
	
	class Meta:
		db_table="Vendor"
	def __str__(self):
		return self.first_name+' '+self.last_name

class Store(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	vendor = models.OneToOneField(to=Vendor, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	registration_number = models.CharField(max_length=50)
	closing_day = models.CharField(max_length=50)
	opening_time = models.CharField(max_length=50)
	closing_time = models.CharField(max_length=50)
	best_seller = models.BooleanField(default=False)
	

	class Meta:
		db_table="Store"
	def __str__(self):
		return self.name

class StoreImages(models.Model):
	store = models.OneToOneField(to=Store, on_delete=models.CASCADE)
	logo = models.ImageField(upload_to='store_logo')
	banner = models.ImageField(upload_to='store_banner')
	image = models.ImageField(upload_to='store_image')
	class Meta:
		db_table="StoreImages"
	def __str__(self):
		return self.store.name+' Images'

class VendorDocs(models.Model):
	vendor = models.OneToOneField(to=Vendor, on_delete=models.CASCADE)
	vendor_idproof_doc_type = models.CharField(max_length=255,null=True, blank=True,)
	vendor_idproof = models.CharField(max_length=255,null=True, blank=True)
	front_idproof = models.FileField(upload_to='store_seller_aadhar_image',null=True, blank=True)
	back_idproof = models.FileField(upload_to='store_seller_aadhar_image',null=True, blank=True)
	store_gst = models.CharField(max_length=50,null=True, blank=True)
	store_msme = models.CharField(max_length=50,null=True, blank=True)
	pancard = models.CharField(max_length=50)
	pancard_image = models.FileField(upload_to='store_seller_pancard_image')
	shiping_policy = RichTextField(null=True, blank=True)
	return_policy = RichTextField(null=True, blank=True)
	bank_account_number = models.CharField(max_length=50)
	bank_name = models.CharField(max_length=100)
	bank_ifsc = models.CharField(max_length=100)
	bank_passbook = models.FileField(upload_to='store_bank_passbook')
	razorpay_id = models.CharField(max_length=200,null=True)
	class Meta:
		db_table="VendorDocs"
	def __str__(self):
		return self.vendor.first_name+' '+self.vendor.last_name

class Product(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	store = models.ForeignKey(Store,on_delete=models.CASCADE,null=True, blank=True)
	vendor_commission = models.FloatField(default=0.0)
	bar_code=models.CharField(max_length=15,null=True,blank=True)
	bar_code_image=models.ImageField(upload_to='Product/BarCode_Img/',null=True, blank=True)
	category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True, blank=True)
	subcategory = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,null=True, blank=True)
	subsubcategory = models.ForeignKey(ProductSubSubCategory,on_delete=models.CASCADE,null=True, blank=True)
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200,null=True, blank=True)
	description =RichTextField(null=True, blank=True)
	mrp = models.FloatField(default=0.0,null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	stock = models.PositiveIntegerField( default=0,null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	product_reject_reason = models.TextField(null=True,blank=True)
	product_rejection = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	offer = models.BooleanField(default=False)
	discount = models.PositiveIntegerField(null=True, default=0)
	featured = models.BooleanField(default=False)
	special_offer = models.BooleanField(default=False)
	special_offer_end_date = models.DateField(blank=True,null=True)

	class Meta:
		db_table="Product"
	def __str__(self):
		return self.name

	

class ProductImages(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
	image = models.FileField(upload_to='products_images',blank=True,null=True)
	class Meta:
		db_table="ProductImages"
	def __str__(self):
		return self.product.name+ 'Images' + str(self.product.id)

class ProductVariant(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
	variant = models.ForeignKey(Variant,on_delete=models.CASCADE, null=True, blank=True)
	variant_value = models.ForeignKey(VariantValue,on_delete=models.CASCADE, null=True, blank=True)
	variant_stock = models.PositiveIntegerField(default=0,blank=True,null=True)
	class Meta:
		db_table="ProductVariant"
	def __str__(self):
		return self.product.name+' '+self.variant.name+'-'+str(self.variant_value.value)

class ProductRating(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	# order = models.ForeignKey(OrderItems, null=True, blank= True, on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	review = models.TextField()
	rating = models.FloatField()
	created_at = models.DateField(auto_now_add=True, null=True)
	class Meta:
		db_table="ProductRating"
	def __str__(self):
		return self.product.name+' Rating '+str(self.rating)

class VendorWithdrawRequest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_withdraw_request')
	request_date = models.DateTimeField()
	amount = models.FloatField()
	is_active = models.PositiveIntegerField(default=0)
	class Meta:
		db_table="VendorWithdrawRequest"
	def __str__(self):
		return 'Withdraw Request of '+str(self.user)


#Model For Business Limit Model
class BusinessLimit(models.Model):
	vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name='business_limit')
	current_balance = models.FloatField(default=0.0)
	class Meta:
		db_table="BusinessLimit"
	def __str__(self):
		return 'BusinessLimit '+str(self.vendor)

class Recharge_Receipt(models.Model):
	receipt_date = models.DateTimeField(auto_now=True)
	vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
	razorpay_order_id = models.CharField(max_length=100)
	payment_id = models.CharField(max_length=200, null=True, blank=True)
	amount = models.FloatField()
	is_active = models.BooleanField(default=False)
	class Meta:
			db_table ="Recharge_Receipt"
	def __str__(self):
			return "Receipt ID "+str(self.id)

#Model for Admin commision amount from Business limit(like wallet) to Admin wallet in case COD 
class BusinessLimitTransaction(models.Model):
	business_limit=models.ForeignKey(BusinessLimit,on_delete=models.CASCADE)
	receipt=models.ForeignKey(Recharge_Receipt,on_delete=models.CASCADE, null=True, blank=True)
	transaction_date = models.DateTimeField()
	transaction_name = models.CharField(max_length=100)
	transaction_type = models.CharField(max_length=20, choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')))
	transaction_amount = models.FloatField()
	previous_amount = models.FloatField()
	remaining_amount = models.FloatField()
	class Meta:
			db_table ="BusinessLimitTransaction"
	def __str__(self):
			return "BusinessLimitTransaction "+str(self.business_limit)

#model for user subscription request
class UserSubscriptionRequest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	month = models.PositiveIntegerField(default=1)
	amount = models.FloatField(default=0.0)
	is_active = models.BooleanField(default=False)
	class Meta:
		db_table = "UserSubscriptionRequest"
	def __str__(self):
		return str(self.user.usr.first_name)+ ' ' +str(self.vendor.first_name)



####################################################################################################################################
#Product calling from ERP 

class Product_Variant(models.Model):
	store = models.CharField(max_length=100, null=True, blank=True)
	product_id = models.CharField(max_length=100, null=True, blank=True)
	category = models.CharField(max_length=100, null=True, blank=True)
	subcategory = models.CharField(max_length=100, null=True, blank=True)
	brand = models.CharField(max_length=100, null=True, blank=True)
	# name = models.CharField(max_length=100, null=True, blank=True)
	# description = models.CharField(max_length=100, null=True, blank=True)
	pruchase_price = models.CharField(max_length=100, null=True, blank=True)
	mrp = models.CharField(max_length=100, null=True, blank=True)
	selling_price = models.CharField(max_length=100, null=True, blank=True)
	price =models.CharField(max_length=100, null=True, blank=True)
	barcode = models.FileField(upload_to='product_barcode_image')
	stock = models.CharField(max_length=100, null=True, blank=True)#Total Stock Including all variants
	size = models.CharField(max_length=100, null=True, blank=True)
	color = models.CharField(max_length=100, null=True, blank=True)
	weight = models.CharField(max_length=100, null=True, blank=True)
	product_reject_reason = models.CharField(max_length=100, null=True, blank=True)
	product_rejection = models.CharField(max_length=100, null=True, blank=True)
	is_active = models.CharField(max_length=100, null=True, blank=True)
	offer = models.CharField(max_length=100, null=True, blank=True)
	discount = models.CharField(max_length=100, null=True, blank=True)
	featured = models.CharField(max_length=100, null=True, blank=True)
	special_offer = models.CharField(max_length=100, null=True, blank=True)
	updated_on = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		db_table = "Product Variant"
	def __str__(self):
		return str(self.user.usr.first_name)+str(self.vendor.first_name)
	
class Product_Variant_Image(models.Model):
	product = models.ForeignKey(Product_Variant, on_delete=models.CASCADE, null=True, blank = True)
	image = models.FileField(upload_to="variant_image")

	class Meta:
		db_table = "Product Variant Image"
	def __str__(self):
		return str(self.product.name) + str(self.image)



######################################################################################################################################


# class Product_erp(models.Model):
# 	product_id = models.CharField(max_length=100, null=True, blank=True)
# 	product_name = models.CharField(max_length=100, null=True, blank=True)
# 	product_barcode = models.ImageField(upload_to='product_barcodes', blank=True)
# 	category = models.CharField(max_length=100, blank=True, null=True)
# 	subcategory = models.CharField(max_length=100, blank=True, null=True)
# 	department = models.CharField(max_length=100, blank=True, null=True)
# 	brand = models.CharField(max_length=100, blank=True, null=True)
# 	is_active = models.BooleanField(default=True)
# 	vendor = models.CharField(max_length=100, blank=True, null=True)
# 	store = models.CharField(max_length=100, blank=True, null=True)
# 	description = models.TextField()
# 	unit_type = models.CharField(max_length=100, blank=True, null=True)
# 	# rename price to purchas
# 	product_img = models.FileField(upload_to='product_img',null=True,blank=True)
# 	variant_created = models.CharField(max_length=100, blank=True, null=True)
# 	barcode_unique_no=models.CharField(max_length=500,null=True,blank=True)
# 	create_at = models.CharField(max_length=100, blank=True, null=True)
# 	update_at = models.CharField(max_length=100, blank=True, null=True)


# 	def __str__(self):
# 		return self.product_name+str(self.id)

# 	# def save(self, *args, **kwargs):
# 	#     EAN = barcode.get_barcode_class('ean13')
# 	#     barcode_no =  random.randint(100000000000, 9999999999999)
# 	#     print("bar code==",barcode_no)  
# 	#     ean = EAN(f'{barcode_no}', writer = ImageWriter())
# 	#     self.barcode_unique_no = ean
# 	#     # print(self.barcode_unique_no,'UUUUUUUUUUUUUUUUUUUUUU')
# 	#     buffer = BytesIO()
# 	#     ean.write(buffer)
# 	#     self.product_barcode.save(f'barcode_unique_no.png', File(buffer), save=False)
# 	#     return super().save(*args, **kwargs)

# class Variant(models.Model):
# 	title = models.CharField(max_length=55)
# 	store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
# 	def __str__(self):
# 		return str(self.title)
    
# class VariantValues(models.Model):
# 	variant = models.ForeignKey(Variant, on_delete=models.CASCADE,blank=True, null=True, default='')
# 	value = models.CharField(max_length=100)

# 	def __str__(self):
# 		r = str(self.value) +"/"+ str(self.id)
# 		return r


# class Product_Variant_Relation(models.Model):
# 	# uuid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)

# 	store = models.CharField(max_length=100, blank=True, null=True)
# 	product = models.ForeignKey(Product_erp, on_delete=models.CASCADE)
# 	variant_values = models.ManyToManyField(VariantValues,null=True,blank=True)

# 	quantity = models.CharField(max_length=100, blank=True, null=True)
# 	purchase_price = models.CharField(max_length=100, blank=True, null=True)
# 	selling_price = models.CharField(max_length=100, blank=True, null=True)
# 	mrp = models.CharField(max_length=100, blank=True, null=True)
# 	product_variant_barcode = models.ImageField(upload_to='product_variant_barcodes', blank=True)
# 	barcode_unique_no=models.CharField(max_length=100, blank=True, null=True)
# 	create_at = models.CharField(max_length=100, blank=True, null=True)
# 	update_at = models.CharField(max_length=100, blank=True, null=True)

# 	def __str__(self):
# 		return str(self.product.product_name) + "   "+ str(self.id)

#     # def save(self, *args, **kwargs):
#     #     EAN = barcode.get_barcode_class('ean13')
#     #     barcode_no =  random.randint(100000000000, 9999999999999)
#     #     ean = EAN(f'{barcode_no}', writer = ImageWriter())
#     #     self.barcode_unique_no = ean
#     #     buffer = BytesIO()
#     #     ean.write(buffer)
#     #     self.product_variant_barcode.save(f'barcode_unique_no.png', File(buffer), save=False)
#     #     return super().save(*args, **kwargs)


# class Product_Image(models.Model):
# 	product = models.ForeignKey(Product_Variant_Relation, on_delete=models.CASCADE)
# 	image = models.FileField(upload_to='product_image',null=True,blank=True)

# 	class Meta:
# 		db_table = 'Product_Image'
