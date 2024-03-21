from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='/'),
    path('contact/',views.contact,name="contacts"),
    path('careerintern/',views.intern,name="careerintern"),
    path('careerintern/career/',views.career,name="career"),
    path('services/',views.service,name="service"),
    path('forms/',views.forms,name="form"),
    path('about/',views.about,name="aboutus"),
]