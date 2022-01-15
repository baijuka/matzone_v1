from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("about/", views.about, name="about"),
   # path("contact_form/", views.contact_form, name="contact_form"),
    path("contact_submit/", views.contact_submit, name="contact_submit"),
]