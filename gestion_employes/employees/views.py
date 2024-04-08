from django.shortcuts import render, get_object_or_404, redirect
from employees.models import Employee
from employees.models import Department
from employees.form import DepartmentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gestion(request):
    departments = Department.objects.all()
    
    # Passer les départements au contexte du template
    context = {
        'departments': departments
    }
    
    return render(request, 'gestion.html', context)

def employee(request):
    employees = Employee.objects.all()
    
    # Passer les employés au contexte du template
    context = {
        'employees': employees
    }
    
    return render(request, 'employee.html', context)

def ajouter_departement(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion')  # Rediriger vers la page de gestion des départements après l'ajout
    else:
        form = DepartmentForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'ajouter-departement.html', context)

def ajouter_employee(request):
    return render(request, 'ajouter_employee.html')


def update_department(request, pk):
    department = get_object_or_404(Department, department_id=pk)
    if request.method == 'POST':
        # Traitement de la mise à jour du département
        return redirect('gestion')  # Rediriger vers la page de gestion des départements
    return render(request, 'update_departement.html', {'department': department})

def delete_department(request, pk):
    department = get_object_or_404(Department, department_id=pk)
    if request.method == 'POST':
        # Traitement de la suppression du département
        department.delete()
        return redirect('gestion')  # Rediriger vers la page de gestion des départements
    return render(request, 'gestion.html', {'department': department})