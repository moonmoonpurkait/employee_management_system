from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    allemp = Employee.objects.all()
    alldept = Department.objects.all()
    allrole = Role.objects.all()
    details ={
        'allemp':allemp,
        'alldept':alldept,
        'allrole':allrole,
    }
    return render(request, 'all_emp.html', details)

def add_emp(request):
        if request.method == 'POST':
            try:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                department = request.POST['department']
                role = request.POST['role']
                salary = request.POST['salary']
                bonus = request.POST['bonus']
                phone_no = request.POST['phone_no']
                hire_date = datetime.now()
                emp = Employee(first_name=first_name, last_name=last_name, dept_id=department, role_id=role, salary=salary, bonus=bonus, phone_no=phone_no, hire_date=hire_date)
                emp.save()
                return HttpResponse("Submission successful.")
            except:
                return HttpResponse("Enter correct data.")
        elif request.method =='GET':
            return render(request, 'add_emp.html')
        else:
            return HttpResponse("Submission Not successful.")

def remove_emp(request,emp_id=0):
    if emp_id:   
        try:  
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return HttpResponse("Successfully deleted.")
        except:
            return HttpResponse("Enter correct id.")
    allemp = Employee.objects.all()
    return render(request, 'remove_emp.html', {'allemp':allemp})

def filter_emp(request):
    if request.method == 'POST':
            name = request.POST['name']
            department = request.POST['department']
            role = request.POST['role']
            emp = Employee.objects.all()
            if name:
                #Q for check multiple fildes
                allemp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
            if department:
                allemp = emp.filter(dept__name=department)
            if role:
                allemp = emp.filter(role__name = role)
            return render(request, 'all_emp.html',{'allemp':allemp})
    elif request.method =='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Enter proper data for filter.")

