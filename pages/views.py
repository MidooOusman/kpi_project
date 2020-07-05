from django.shortcuts import render
from django.http import HttpResponse 
from employees.models import Employee
from managers.models import Manager
from employees.choices import price_choices, bedroom_choices, state_choices
def index (request):
    employees = Employee.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'employees': employees,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render (request, 'pages/index.html', context )

def about (request):
    # Get all managers
    managers = Manager.objects.order_by('-hire_date')

    #Get MVP 
    mvp_managers = Manager.objects.all() .filter(is_mvp= True)

    context = {
        'managers': managers,
        'mvp_managers': mvp_managers
    }

    return render (request, 'pages/about.html', context)