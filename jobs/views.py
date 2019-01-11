from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})

def portfolio_list(request):
    jobs = Job.objects
    return render(request, 'jobs/portfolio.html',{'jobs':jobs})
