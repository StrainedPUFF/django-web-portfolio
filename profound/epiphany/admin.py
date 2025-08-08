from django.contrib import admin
from .models import Projects, BlogPost, Testimonial, ContactMessage, UserProfile
# Register your models here.
admin.site.register([Projects, BlogPost, Testimonial, ContactMessage, UserProfile])