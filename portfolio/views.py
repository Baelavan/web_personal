from django.shortcuts import render
from .models import Project

def home(request):
    featured_projects = Project.objects.filter(featured=True)
    return render(request, 'portfolio/home.html', {
        'featured_projects': featured_projects
    })

def portfolio_category(request, category):
    projects = Project.objects.filter(category=category)
    return render(request, 'portfolio/category.html', {
        'projects': projects,
        'category': category
    })

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')