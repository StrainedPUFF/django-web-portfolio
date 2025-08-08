# """
# URL configuration for profound project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from epiphany.views import (ProjectsView, BlogPostView, TestimonialView, ContactMessageView, UserProfileView, PortfolioHomeView, UserProfilecVview)
from epiphany.views import (PortfolioHomeView, PortfolioProjectsView, PortfolioUserProfileView, PortfolioContactMessageView, PortfolioBlogPostView, PortfolioTestimonialView, PortfolioBioView, PortfolioCV_View)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', PortfolioHomeView.as_view(), name='portfolio-home'),
    path('home/projects/', PortfolioProjectsView.as_view(), name='portfolio-projects'),
    path('home/blogposts/', PortfolioBlogPostView.as_view(), name='portfolio-blogposts'),
    path('home/testimonials/', PortfolioTestimonialView.as_view(), name='portfolio-testimonials'),
    path('home/contactmessages/', PortfolioContactMessageView.as_view(), name='portfolio-contactmessages'),
    path('home/user_profile/', PortfolioUserProfileView.as_view(), name='portfolio-user_profile'),
    path('home/user_profile/bio', PortfolioBioView.as_view(), name='portfolio-user-bio'),
    path('home/user_profile/cv', PortfolioCV_View.as_view(), name='portfolio-user-cv'),
]
if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    