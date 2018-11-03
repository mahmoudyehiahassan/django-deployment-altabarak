from django import forms
from .models import Document, ContactUs
from django.utils.translation import gettext_lazy as _


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'empemail',
         		 'phonenumber',)
        labels = {'description' : _('الاسم'),
        		'empemail' : _('البريد الالكترونى'),
        		'phonenumber' : _('رقم الهاتف'),
        		'document' : _('السيرة الذاتية')}


class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = ('fullname', 'e_mail', 'text',)
		labels = {'fullname' : _('الاسم'), 'e_mail' : _('البريد الالكترونى'),
				'text' : _('نص الرساله')}


