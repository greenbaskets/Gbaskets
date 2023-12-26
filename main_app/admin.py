from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.utils.html import format_html
	
admin.site.site_header="AVPL ADMIN"
admin.site.site_title="AVPL Admin Panel"
admin.site.index_title="Welcome to AVPL Admin Panel"

from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 
                           'groups', 'user_permissions')
        else:
            # modify these to suit the fields you want your
            # staff user to be able to edit
            perm_fields = ('is_active', 'is_staff')

        return [(None, {'fields': ('username', 'password')}),
                (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (('Permissions'), {'fields': perm_fields}),
                (('Important dates'), {'fields': ('last_login', 'date_joined')})]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

class LevelsAdmin(admin.ModelAdmin):
	list_display = ['level']

class RoleAdmin(admin.ModelAdmin):
	list_display = ['user', 'level']

class AdminMLM(admin.ModelAdmin):
	list_display = ['child']

class MLM_Admin(admin.ModelAdmin):
	list_display = ['parent', 'node', 'left', 'right']

class RazorpayAdmin(admin.ModelAdmin):
	list_display = ['payment_id', 'order_id', 'signature']

class Level_Admin(admin.ModelAdmin):
	list_display = [ 'referrals','level_plan_referral','level_plan_sponsor' ,]

admin.site.register(Main_SITE_URL)
admin.site.register(Levels,LevelsAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(MLMAdmin,AdminMLM)
admin.site.register(MLM,MLM_Admin)
admin.site.register(RazorpayTransaction,RazorpayAdmin)

admin.site.register(RazorpayOrder)
admin.site.register(Wallet)
admin.site.register(WalletTransaction)
admin.site.register(Min_Amount_For_Free_Delivery)
admin.site.register(contact_us)

admin.site.register(GST_Log)
admin.site.register(OrderItems)
admin.site.register(Orders)
admin.site.register(TDS_Log)
admin.site.register(termsandcondition)
admin.site.register(privacypolicy)
admin.site.register(PV_data)
admin.site.register(WalletTransfer)
admin.site.register(WalletTransferApproval)
admin.site.register(Reason)
admin.site.register(Notification)

admin.site.register(Level_Plan_Sponsors)
admin.site.register(Level_Plan_Referrals,Level_Admin)
admin.site.register(UserLinkType)
admin.site.register(TDS_Log_Wallet)














