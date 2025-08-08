from django.db import models
import logging
logger = logging.getLogger(__name__)

class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(unique=True)
    image = models.ImageField(upload_to = 'projects/') 
    link = models.URLField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if Projects.objects.exclude(pk=self.pk).filter(title=self.title).exists():
            logger.warning("Project title already exist. Please double check your input.")
            return
        if self.link and Projects.objects.exclude(pk=self.pk).filter(link=self.link).exists():
            logger.warning("Project link already exists. Please double check your input.")
            return
        if self.description and Projects.objects.exclude(pk=self.pk).filter(description=self.description).exists():
            logger.warning("A similar description already exists. Please input a valid description")
            return
        super().save(*args, **kwargs)

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    def save (self, *args, **kwargs):
        # if BlogPost.objects.filter(title=self.title).exists():
        #     logger.warning("A blog with a similar title already exists. Please input another title")
        #     return
        # if self.content and BlogPost.objects.filter(content=self.content).exists():
        #     logger.warning("Similar content already exists. please insert new content")
        #     return
        if BlogPost.objects.exclude(pk=self.pk).filter(title=self.title).exists():
            logger.warning("The title you entered already exists. Please input a different title.")
            return
        if self.content and BlogPost.objects.exclude(pk=self.pk).filter(content=self.content).exists():
            logger.warning("Similar content can not be submitted twice. Please check your input")
            return
        super().save(*args, **kwargs)
    
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    quote = models.TextField(unique=True)
    role = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} ({self.role})"
    
    def save(self, *args, **kwargs):
        # if Testimonial.objects.filter(quote=self.quote).exists():
        #     logger.warning("A similar quote already exists. Please insert new content")
        #     return
        if Testimonial.objects.exclude(pk=self.pk).filter(quote=self.quote).exists():
            logger.warning("A similar quote already exists. Please check and or change your input.")
            return
        else:
            super().save(*args, **kwargs)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    message = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}: {self.email}"
    
    def save(self, *args, **kwargs):
        # if ContactMessage.objects.filter(message=self.message).exists():
        #     logger.warning("A similar message already exists. Please insert a new message")
        #     return
        if ContactMessage.objects.exclude(pk=self.pk).filter(message=self.message).exists():
            logger.warning("A similar message already exists. Please check and or change your message")
            return
        else:
            super().save(*args, **kwargs)
from django.contrib.auth.models import User
class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    display_photo = models.ImageField(upload_to='profile_pic_uploads')
    curriculum_vitae = models.TextField()
    Bio = models.TextField()
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # if UserProfile.objects.filter(name=self.name).exists():
        #     logger.warning("The name already exists")
        #     return
        # else:
        if UserProfile.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            logger.warning("A user with the same name already exists. Please use other names or check your input.")
            return
        else:
            super().save(*args, **kwargs)
    def __str__(self):
        return self.name