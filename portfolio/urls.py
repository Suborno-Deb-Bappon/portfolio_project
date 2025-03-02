from django_distill import distill_path
from . import views

def get_no_args():
    return None

urlpatterns = [
    distill_path('', views.index, name='index', distill_func=get_no_args),
    distill_path('about/', views.about, name='about', distill_func=get_no_args),
    distill_path('experience/', views.experience, name='experience', distill_func=get_no_args),
    distill_path('education/', views.education, name='education', distill_func=get_no_args),
    distill_path('projects/', views.projects, name='projects', distill_func=get_no_args),
    distill_path('publications/', views.publications, name='publications', distill_func=get_no_args),
    distill_path('certifications/', views.certifications, name='certifications', distill_func=get_no_args),
    distill_path('awards/', views.awards, name='awards', distill_func=get_no_args),
    distill_path('extracurricular/', views.extracurricular, name='extracurricular', distill_func=get_no_args),
    distill_path('contact/', views.contact, name='contact', distill_func=get_no_args),
]
