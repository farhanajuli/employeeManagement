from django.shortcuts import render, HttpResponse, redirect
from .models import Employee, Role, Department, Client, Project, User
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib import messages


# signup, login, logout
@login_required(login_url='login')
def signUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'employees/signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'employees/login.html')

def logoutPage(request):
	logout(request)
	return redirect('login')
    


# Dashboard 
def dashboard(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'employees/dashboard.html',context)


# Department
def all_dept(request):
    depts = Department.objects.all()
    context = {
        'depts': depts
    }
    return render(request, 'departments/all_dept.html', context)

def add_dept(request):
    depts = Department.objects.all()
    
    if request.method == 'POST':
        dept_name = request.POST.get('dept_name')
        
        Department.objects.create(dept_name=dept_name)
        messages.success(request, 'New Department created successfully')
    context = {
        "depts": depts,
    }
    
    return render(request, 'departments/add_dept.html', context)
    
def edit_dept(request,id):
    dept = Department.objects.get(id=id)
    
    if request.method == 'POST':
        dept_name = request.POST.get('dept_name')
        
        dept.dept_name = dept_name
        
        dept.save()
        messages.success(request, 'Department edited successfully')
        return redirect('all_dept')
    context = {
        "dept": dept,
    }
    return render(request, 'departments/edit_dept.html', context)

def remove_dept(request,id):
    dept = Department.objects.get(id=id)
    dept.delete()
    return redirect('all_dept')
    
    

#Role
def all_role(request):
    roles = Role.objects.all()
    context = {
        'roles': roles
    }
    return render(request, 'roles/all_role.html', context)

def add_role(request):
    roles = Role.objects.all()
    
    if request.method == 'POST':
        role_name = request.POST.get('role_name')
        
        Role.objects.create(role_name=role_name)
        messages.success(request, 'Role created successfully')
        
        
    context = {
        "roles": roles,
    }
    
    return render(request, 'roles/add_role.html', context)

def edit_role(request,id):
    role = Role.objects.get(id=id)
    
    if request.method == 'POST':
        role_name = request.POST.get('role_name')
        
        role.role_name = role_name
        
        role.save()
        messages.success(request, 'Role edited successfully')
        return redirect('all_role')
    context = {
        "role": role,
    }
    return render(request, 'roles/edit_role.html', context)

def remove_role(request,id):
    role = Role.objects.get(id=id)
    role.delete()
    return redirect('all_role')



# Employee
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'employees/view_all_emp.html', context)
    
def add_emp(request):
    depts = Department.objects.all()
    roles = Role.objects.all()
   
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dept_name = request.POST.get('dept_name')
        role_name = request.POST.get('role_name')
        dept_instance = Department.objects.get(dept_name=dept_name)
        role_instance = Role.objects.get(role_name=role_name)
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        hire_date = request.POST.get('hire_date')

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            dept = dept_instance,
            role= role_instance,
            salary=salary,
            bonus=bonus,
            hire_date=hire_date,
        )
        messages.success(request, 'Employee added successfully')
    context = {
         "depts": depts,
         "roles": roles,
        } 
    return render(request, 'employees/add_emp.html',context)
    
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, 'Employee removed successfully')
        except:
            messages.warning(request, 'Please Enter A Valid Employee ID')
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'employees/remove_emp.html', context)

def filter_emp(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__dept_name__icontains=dept)
        if role:
            emps = emps.filter(role__role_name__icontains=role)

        context = {
            'emps': emps,
        }
        return render(request, 'employees/view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'employees/filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')

def edit_emp(request,id):
    emp = Employee.objects.get(id=id)
    depts = Department.objects.all()
    roles = Role.objects.all()
    
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dept_name = request.POST.get('dept_name')
        role_name = request.POST.get('role_name')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        hire_date = request.POST.get('hire_date')
        dept_instance = Department.objects.get(dept_name=dept_name)
        role_instance = Role.objects.get(role_name=role_name)
        
        
        emp.first_name = first_name
        emp.last_name = last_name
        emp.email = email
        emp.phone = phone
        emp.dept = dept_instance
        emp.role = role_instance
        emp.salary = salary
        emp.bonus = bonus
        emp.hire_date =hire_date
        
        emp.save()
        messages.success(request, 'Employee edited successfully')
        return redirect('all_emp')
    
    context = {
        "emp" : emp,
        "depts": depts,
        "roles": roles,
    }
    
    return render(request, 'employees/edit_emp.html', context)
		    
def emp_details(request,emp_id=0):
    emp = Employee.objects.get(id=emp_id)
    context = {
        'emp': emp,
    }
    return render(request,'employees/emp_details.html',context)

def payslip(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    template_path = 'payroll/payslip.html'
    context = {
        'emp': emp,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def employee_list(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'payroll/employee_list.html', context)



# Client
def all_client(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/all_client.html', context)

def add_client(request):
    
    clients = Client.objects.all()
    
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        client_phone = request.POST.get('client_phone')
        gender = request.POST.get('gender')
        website = request.POST.get('website')
                                  
        Client.objects.create(
            client_name=client_name,
            client_email=client_email,
            client_phone=client_phone,
            gender=gender,
            website = website,
        )
        messages.success(request, 'Client added successfully')
    context= {
        "clients": clients
    } 
    return render(request, 'clients/add_client.html', context=context)

def remove_client(request, client_id=0):
    if client_id:
        try:
            client_to_be_removed = Client.objects.get(id=client_id)
            client_to_be_removed.delete()
            messages.success(request, 'Client removed successfully')
        except:
            messages.warning(request, 'Please Enter A Valid Client ID')
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/remove_client.html', context=context)

def edit_client(request,id):
    client = Client.objects.get(id=id)
    
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        client_phone = request.POST.get('client_phone')
        gender = request.POST.get('gender')
        website = request.POST.get('website')
        
        
        client.client_name = client_name
        client.client_email = client_email
        client.client_phone = client_phone
        client.gender = gender
        client.website = website
        
        client.save()
        messages.success(request, 'Client details edited successfully')
        return redirect('all_client')
    context = {
        "client": client
    }
    return render(request, 'clients/edit_client.html', context)
    
    
    



# projects
def all_project(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/all_project.html', context)

def add_project(request):
    depts = Department.objects.all()
    clients = Client.objects.all()
    
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        client_name = request.POST.get('client_name')
        dept_name = request.POST.get('dept_name')
        project_details = request.POST.get('project_details')
        amount = request.POST.get('amount')
        priority = request.POST.get('priority')
        client_instance = Client.objects.get(client_name=client_name)   
        dept_instance = Department.objects.get(dept_name=dept_name)                 
        
        
        Project.objects.create(
            project_name=project_name,
            client_name=client_instance,
            dept = dept_instance,
            project_details=project_details,
            amount=amount,
            priority=priority,
        )
        messages.success(request, 'Hurrah! New Project added successfully')
        
    context= {
        "depts": depts,
        "clients": clients,
    } 
    return render(request, 'projects/add_project.html', context=context)  

def edit_project(request, id):
    project = Project.objects.get(id=id)
    depts = Department.objects.all()
    
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        amount = request.POST.get('amount')
        priority = request.POST.get('priority')
        project_details = request.POST.get('project_details')
        dept_name = request.POST.get('dept_name')
        dept_instance = Department.objects.get(dept_name=dept_name)
        
        
        project.project_name = project_name
        project.amount = amount
        project.priority = priority
        project.project_details = project_details
        project.dept = dept_instance
        
        project.save()
        messages.success(request, 'Project details edited successfully')
        return redirect('all_project')
    context = {
        "project": project,
        "depts": depts,
    }
    return render(request, 'projects/edit_project.html', context)

   
def remove_project(request, project_id=0):
    if project_id:
        try:
            project_to_be_removed = Project.objects.get(id=project_id)
            project_to_be_removed.delete()
            messages.success(request, 'Project removed successfully')
        except:
            messages.warning(request, 'Please Enter A Valid Project ID')
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/remove_project.html', context=context)