from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='employees'),
    path('<int:employee_id>', views.employee, name='employee'),
    path('search', views.search, name='search'),
]

