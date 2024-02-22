from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dept_name


class Role(models.Model):
    role_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.role_name
    
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank= True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateTimeField(blank = True, null = True)
    
    def total_salary(self):
        return int(self.salary + self.bonus)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Client(models.Model):
    client_name = models.CharField(max_length=255, null= False)
    client_email = models.EmailField(max_length=255, blank = True)
    client_phone = models.IntegerField(default=0)
    gender= models.CharField(max_length=255, null= False)
    website = models.CharField(max_length=255)
    
    def __str__(self):
        return self.client_name
    
    
    
class Project(models.Model):
    project_name = models.CharField(max_length= 100, null= True)
    project_details = models.TextField(blank=True, max_length=255)
    amount = models.IntegerField(default=0)
    priority = models.CharField(max_length=100,null=True, blank=True)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.project_name
