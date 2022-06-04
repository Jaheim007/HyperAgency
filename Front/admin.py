from django.contrib import admin
from .models import Slider, Contact, SiteInfo, Service, Testimonial

@admin.register(Slider)
class Slide(admin.ModelAdmin):
    list_display = ('title','address','address_number','image')

@admin.register(Contact)
class ContactInfo(admin.ModelAdmin):
    list_display = ('fb_link','insta_link','twitter_link', 'linkedin_link', 'site_contact', 'email', 'latitude', 'longitude' )

@admin.register(SiteInfo)
class Site(admin.ModelAdmin):
     list_display = ('title1','title2', 'main_color', 'full_site_color', 'default_mode')

@admin.register(Service)
class Service(admin.ModelAdmin):
     list_display = ('service_name', 'service_description')

@admin.register(Testimonial)
class Test(admin.ModelAdmin):
     list_display = ('name', 'description', 'image')
     


# Register your models here.
