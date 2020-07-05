from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
 
from .models import Employee

def index (request):
   employees = Employee.objects.order_by('-list_date').filter(is_published=True)

   paginator =Paginator(employees, 3)
   page = request.GET.get('page')
   paged_employees = paginator.get_page(page)

   context = {
      'employees': paged_employees

   }

   return render(request,'employees/employees.html', context)

def employee (request, employee_id):
   employee = get_object_or_404( Employee, pk=employee_id)

   context = {
      'employee': employee
   }

   return  render(request,'employees/employee.html', context) 

def search (request):
   queryset_list = Employee.objects.order_by('-list_date')
   
   #Keywords
   
   if 'keywords' in request.GET:
      keywords= request.GET['keywords']
      if keywords:
         queryset_list = queryset_list.filter(titel__icontains=keywords)
   
   #city
   
   if 'city' in request.GET:
      city= request.GET['city']
      if city:
         queryset_list = queryset_list.filter(city__iexact=city)

   #state
   
   if 'state' in request.GET:
      state= request.GET['state']
      if state:
         queryset_list = queryset_list.filter(state__iexact=state)


  
   #bedroom
   
   if 'bedrooms' in request.GET:
      bedrooms= request.GET['bedrooms']
      if bedrooms:
         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


   #price
   
   if 'price' in request.GET:
      price= request.GET['price']
      if price:
         queryset_list = queryset_list.filter(price__iexact=price)


   context = {
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'employees': queryset_list,
      'values': request.GET
      }


   return render(request,'employees/search.html', context)