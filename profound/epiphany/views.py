from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import BlogPost, Testimonial, Projects, ContactMessage, UserProfile

class PortfolioHomeView(TemplateView):
    template_name = 'templates/portfolio_home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Projects.objects.all()                                                                                                                                                                                                                        
        context['blogpost'] = BlogPost.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['contactmessages'] = ContactMessage.objects.all()
        context['user_profile'] = UserProfile.objects.all()
        # context['user-cv'] = UserProfile.objects.curriculum_vitae
        return context
    
class PortfolioProjectsView(ListView):
    template_name = 'templates/portfolio_section.html'
    model = Projects
    section_title = 'projects'    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = self.section_title
        context['items'] = self.model.objects.all()
        for item in context['items']:
            item.object_type =self.model.__name__
        return context

class PortfolioUserProfileView(ListView):
    template_name = 'templates/portfolio_section.html'
    model = UserProfile
    section_title = 'user-profile'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['section_title'] = self.section_title
        context['items'] = self.model.objects.all()
        for item in context['items']:
            item.object_type = self.model.__name__
        return context

class PortfolioTestimonialView(ListView):
    template_name = 'templates/portfolio_section.html'
    model = Testimonial
    section_title = 'testimonials'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = self.section_title
        context['items'] = self.model.objects.all()
        for item in context['items']:
            item.objects_type = self.model.__name__
        return context

class PortfolioBlogPostView(ListView):
    template_name = 'templates/portfolio_section.html'
    model = BlogPost
    section_title = 'blogposts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = self.section_title
        context['items'] = self.model.objects.all()
        for items in context['items']:
            item.object_type = self.model.__name__
        return context
    
class PortfolioContactMessageView(ListView):
    template_name = 'templates/portfolio_section.html'
    model = ContactMessage
    section_title = 'contact_messages'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = self.section_title
        context['items'] = self.model.objects.all()
        for item in context['items']:
            item.object_type = self.model.__name__
        return context

class PortfolioBioView(TemplateView):
    template_name = 'templates/portfolio_section.html'
    section_title = 'Bio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.first()
        context['section_title'] = self.section_title
        context['items'] = [user_profile]
        return context
    
class PortfolioCV_View(TemplateView):
    template_name = 'templates/portfolio_section.html'
    section_title = 'Curriculum Vitae'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.first()
        context['section_title'] = self.section_title
        context['items'] = [user_profile]
        return context
# class ProjectsView(PortfoliosectionView):
#     model = Projects
#     section_title = 'projects'
    
# class UserProfilecVview(PortfolioSectionView):
#     model = UserProfile
#     section_title = 'user-cv'
    
# class BlogPostView(PortfolioSectionView):
#     model = BlogPost
#     section_title = 'blogposts'

# class TestimonialView(PortfolioSectionView):
#     model = Testimonial
#     section_title = 'testimonials'

# class ContactMessageView(PortfolioSectionView):
#     model = ContactMessage
#     section_title = 'contactmessages'
    
# class UserProfileView(PortfolioSectionView):
#     model = UserProfile
#     section_title = 'user_profile'
    
# class PortfolioSectionView(ListView):
#     template_name = 'templates/'
    
#     def get_queryset(self, **kwargs)
#         return self.model.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context('section_title') = self.section_title
#         context('items') = context['object_list']
#         return context
    
# class PortfolioSecView(ListView):
#     template_name = 'projects/'
    
#     def get_queryset(self):
#         return self.model.objects.all()
    
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data()#
#     #     context['section_title'] = self.section_title
#     #     context['items'] = context['objects_list']
#     #     return context


# class PortfolioHomeView(TemplateView):
#     template_name = 'templates/portfolio_home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['projects'] = Projects.objects.all()
#         context['user_profile'] = UserProfile.objects.all()
#         context['blogposts'] = BlogPost.objects.all()
#         context['testimonials'] = Testimonial.objects.all()
#         context['contactmessages'] = ContactMessage.objects.all()
#         return context
    
# class PortfolioSectionView(ListView):
#     template_name = 'templates/portfolio_home.html'
    
#     def get_queryset(self):
#         return self.model.objects.all()
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['section_title'] = self.section_title
#         context['items'] = context['objects_list']
#         return context 