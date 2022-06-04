from django.shortcuts import render
from .models import * 
from Customers.models import Customer

def index(request):
    is_activated = True
    slider = Slider.objects.all()
    service = Service.objects.all()
    test = Testimonial.objects.all()
    return render(request,'pages/index.html' , locals())
    
def about(request):
    about = True
    
    return render(request,'pages/about.html', locals())

def property(request):
    property = True
    
    return render(request,'pages/property.html', locals())

def contact(request):
    contact = True
    
    return render(request,'pages/contact.html', locals())

def blog_grid(request):
    blog = True
    
    return render(request,'pages/blog-grid.html', locals())

def agents_grid(request):
    agents = True
    info = Customer.objects.all()
    return render(request,'pages/agents-grid.html')

def agents_single(request):
    agents_single= True
    
    return render(request,'pages/agent-single.html')

def blog_single(request):
    blog_single = True
    
    return render(request,'pages/blog-single.html')

def property_grid(request):
    property_grid = True
    
    return render(request,'pages/property-grid.html')

# Create your views here.
