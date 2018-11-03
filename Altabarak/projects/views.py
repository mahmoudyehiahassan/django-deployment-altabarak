from django.shortcuts import render, redirect, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .models import senddata
from .models import Document
from .forms import DocumentForm, ContactUsForm
from django.contrib import messages
from django.utils.html import format_html, html_safe

# Create your views here.

def projects_list(request):
	return render(request, 'projects/hospitals.html')

def aboucom(request):
    return render(request, 'projects/about_us.html')

def allBanks(request):
    return render(request, 'projects/banks.html')

def institute(request):
	return render(request, 'projects/Colleges&Institutes.html')

def allbuilding(request):
    return render(request, 'projects/Public_buildings.html')

def Factories(request):
	return render(request, 'projects/Factories.html')

def Schools(request):
	return render(request, 'projects/Schools.html')

def Residential(request):
	return render(request, 'projects/Residential_Projects.html')

def our_job(request):

	# job is a object from 'senddata class in models.py'
	job = senddata.objects.all()
	context = {'job':job}
	return render(request, 'projects/jobs.html', context)


##########################################


def testupload(request):
    documents = Document.objects.all()
    #context = {'documents' : documents}
    return render(request, 'projects/homeupload.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'projects/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'projects/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form_description = form.cleaned_data.get('description')
            form_document = form.cleaned_data.get('document')
            form_empemail = form.cleaned_data.get('empemail')
            form_phonenumber = form.cleaned_data.get('phonenumber')
            form.save()
            messages.success(request, 'تم ارسال البيانات بنجاح , نشكركم للتسجيل بشركتنا, سوف يتم التواصل بحضرتكم')
    else:
        form = DocumentForm()
    return render(request, 'projects/model_form_upload.html', {
        'form': form
    })


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form_fullname = form.cleaned_data.get('fullname')
            form_e_mail = form.cleaned_data.get('e_mail')
            form_text = form.cleaned_data.get('text')
            form.save()
            messages.success(request, 'تم ارسال البيانات بنجاح شكرا لاهتمامكم سوف يتم الرد على رسالتكم')
    else:
        form = ContactUsForm()
    return render(request, 'projects/contact_us.html', {
        'form' : form
        })
