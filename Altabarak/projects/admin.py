from django.contrib import admin
from .models import senddata, ContactUs, Document
# Register your models here.

class senddataadmin(admin.ModelAdmin):
	list_display = ["__str__", "Edu_Qualification", "years_of_Experience"]
	class Meta:
		model = senddata 

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['description', 'empemail', 'phonenumber','uploaded_at']
    class Meta:
    	model = Document


class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['fullname', 'e_mail', 'text', 'pub_date']
	class Meta:
		model = ContactUs


admin.site.register(senddata, senddataadmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
