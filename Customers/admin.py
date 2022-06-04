from django.contrib import admin
from .models import InfoAgent, Customer


@admin.register(InfoAgent)
class Info(admin.ModelAdmin):
    list_display = ('customer', 'Biographie', 'fb_link', 'insta_link', 'twitter_link', 'linkedin_link')

@admin.register(Customer)
class Custom(admin.ModelAdmin):
    list_display = ('user',  'phone', 'image', 'birth_date', 'user_type')

# Register your models here.
