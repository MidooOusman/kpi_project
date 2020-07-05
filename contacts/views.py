from django.shortcuts import render, redirect 
from django.contrib import messages
from . models import Contact 
from django.core.mail import send_mail


def contact (request):
 if request.method == 'POST':
     employee_id = request.POST ['employee_id']
     employee = request.POST ['employee']
     name = request.POST ['name']
     phone = request.POST ['phone']
     message = request.POST ['message']
     user_id = request.POST ['user_id']
     email = request.POST ['email']
     
     
     if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(employee_id=employee_id,user_id=user_id)
        if has_contacted:
           messages.error(request, 'You have already made an inquiryfor this Employee')
        return redirect ('/employees/'+employee_id)

     
     contact = Contact(employee=employee, employee_id=employee_id, name=name, email=email,phone=phone,message=message,user_id=user_id )

     contact.save()

     #send email
     send_mail(
        'Employee listing inquiry from  ' + employee,
        'There has been an inquiry for '+ employee + '. Sign in into the admin panel for more info',
        'midoo6491@gmail.com',
        [email, 'maht_6491@hotmail.com'],
        fail_silently= False 
     )

     messages.success (request, 'Your request has been submitted, a realtor will get back to you soon')

     return redirect ('/employees/'+employee_id)