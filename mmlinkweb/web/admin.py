from django.contrib import admin
from django.utils.html import format_html

from .models import*
# Register your models here.



admin.site.site_header = "Myanmar Link"
admin.site.site_title = "Myanmar Link"




class ComplainAdmin(admin.ModelAdmin):
	list_display = ("name", 'customer_id', 'router', 'phone_number', 'address', 'comment', 'create_at', 'status', '_'
				)
	list_filter = ('customer_id', 'name', 'status')
	list_per_page = 10
	
	def _(self, obj):
		if obj.status == 'Read':
			return True
		else:
			return False
	_.boolean = True


	def status(self, obj):
		if obj.status == 'Read':
			return '#80c904'
		else:
			return 'red'
		return format_html('<strong><p style="color:red">{}</p></strong>'.format(color, obj.status))

	status.allow_tags = True



class NewInstallationAdmin(admin.ModelAdmin):
	list_display = ( "name", "phone_number", "address", "about", "create_at")
	list_filter = ("name", "phone_number")
	list_per_page = 10



class BillingAdmin(admin.ModelAdmin):
	list_filter = ("name", "customer_id")
	list_display = ("name", "customer_id", "bill_screenshot", "remark", "create_at", "status", "_")
	list_per_page = 10


	def _(self, obj):
		if obj.status == 'Read':
			return True
		else:
			return False
	_.boolean = True


	def status(self, obj):
		if obj.status == 'Read':
			return '#80c904'
		else:
			return 'red'
		return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color, obj.status))

	status.allow_tags = True

		
		
		


class BillingstatusAdmin(admin.ModelAdmin):
	list_display =("name", "error_status", "pending_status", "finishing_status", "remark", "create_at", "update_at")
	list_filter = ("error_status", "pending_status", "finishing_status")
	search_fields = ("error_status", "pending_status", "finishing_status")
	list_per_page = 10



class NewinstallationStatusAdmin(admin.ModelAdmin):
	list_display = ("name", "full_box", "no_box", "customer_cancel", "done")
	list_per_page = 10





admin.site.register(Complain, ComplainAdmin)

admin.site.register(NewInstallation, NewInstallationAdmin)
admin.site.register(NewinstallationStatus, NewinstallationStatusAdmin)

admin.site.register(Internetplan)


admin.site.register(Billing, BillingAdmin)
admin.site.register(Billingstatus, BillingstatusAdmin)

