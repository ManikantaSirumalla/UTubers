from django.shortcuts import render,redirect
from .models import Contactutubers

# Create your views here.
from django.contrib import messages

def contactutubers (request) :
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        detail_message = request.POST['detail_message']

        contactutubers = Contactutubers(full_name=full_name,  phone=phone, email=email, company_name=company_name, subject=subject, detail_message=detail_message)
        contactutubers.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')