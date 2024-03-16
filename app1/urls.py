from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='/'),
    path('contact/',views.contact,name="contacts"),
    path('careerintern/',views.career,name="careerintern"),
]