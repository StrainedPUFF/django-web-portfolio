from django.urls import path
from .views import (
    ProjectsView, BlogPostView
    TestimonialView, ContactMessageView
)


urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='portfolio-projects'),
    path('blogposts/', BlogPostView.as_view(), name='portfolio-blogposts'),
    path('testimonials/', TestimonialView.as_view(), name='portfolio-testimonials'),
    path('contactmessages/', ContactMessageView.as_view(), name='portfolio-contactmessages'),
]