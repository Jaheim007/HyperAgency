from django.db import models

class SiteInfo(models.Model):     
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    main_color = models.CharField(max_length=255)
    full_site_color = models.CharField(max_length=255)
    default_mode = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title1

class Contact(models.Model): 
    fb_link = models.URLField(null=True)
    insta_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    site_contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)  
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5 , decimal_places=2)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fb_link
        
class Slider(models.Model):
    title = models.CharField(max_length = 255)
    address= models.CharField(max_length = 255)          
    address_number = models.CharField(max_length = 255)     
    image = models.URLField()
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    service_name = models.CharField(max_length = 255)
    service_description = models.TextField(max_length = 500) 
    
    def __str__(self):
        return self.service_name
    
class Testimonial(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    image = models.URLField(max_length = 500)
# Create your models here.
