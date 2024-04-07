from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gestion(request):
    return render(request, 'gestion.html')

def employee(request):
    return render(request, 'employee.html')

def ajouter_departement(request):
    return render(request, 'ajouter-departement.html')

def ajouter_employee(request):
    return render(request, 'ajouter_employee.html')
