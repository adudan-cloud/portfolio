from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/base.html')

def about(request):
    return render(request, 'home/about.html')

def projects(request):
    return render(request, 'home/projects.html')