from django.urls import path

from .views import *

urlpatterns = [
    path('dashboard/',dashboard, name='dashboard'),
    path('all_emp/',all_emp, name='all_emp'),
    path('add_emp/',add_emp, name='add_emp'),
    path('remove_emp/',remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>',remove_emp, name='remove_emp'),
    path('edit_emp/<int:id>', edit_emp, name="edit_emp"),
    path('filter_emp/',filter_emp, name='filter_emp'),
    path('emp_details/<int:emp_id>', emp_details, name="emp_details"),
    
    path('',signUpPage,name='signup'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    
    path('add_dept/', add_dept, name='add_dept'),
    path('all_dept/', all_dept, name='all_dept'),
    path('edit_dept/<int:id>', edit_dept, name="edit_dept"),
	path('remove_dept/<int:id>', remove_dept, name="remove_dept"),
 
    path('add_role/', add_role, name='add_role'),
    path('all_role/', all_role, name='all_role'),
    path('edit_role/<int:id>', edit_role, name="edit_role"),
	path('remove_role/<int:id>', remove_role, name="remove_role"),
 
 
    path('add_client/',add_client, name='add_client'),
    path('edit_client/<int:id>', edit_client, name="edit_client"),
    path('remove_client/',remove_client,name='remove_client'),
    path('remove_client/<int:client_id>',remove_client, name='remove_client'),
    path('all_client/',all_client, name='all_client'),
    
    
    path('payslip/<int:emp_id>',payslip, name='payslip'),
    path('employee_list/',employee_list, name='employee_list'),
    
    
    path('all_project/',all_project,name='all_project'),
    path('add_project/',add_project, name='add_project'),
    path('remove_project/',remove_project,name='remove_project'),
    path('remove_project/<int:project_id>',remove_project, name='remove_project'),
    path('edit_project/<int:id>',edit_project, name='edit_project'),
    
]
