from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def new_project(request):
    return render(request, 'main/new_project.html')

def deployment(request):
    return render(request, 'main/deployment.html')

def redeployment(request):
    return render(request, 'main/redeployment.html')
