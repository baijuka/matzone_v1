from django.shortcuts import render, redirect, reverse
from products.models import Product
from .models import Contact
from django.contrib import messages


# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, "home/index.html")


def about(request):
    """A view to return the about page"""
    return render(request, "home/about.html")


def contact_submit(request):
    """A view to return the contact page"""
    if request.method == "POST":
        contact = Contact()
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        contact.message = message
        contact.save()
        messages.success(
            request,
            f"Your message has been sent, thank you for contacting us!",
        )
    return redirect(reverse("home"))


def contact_form(request):
    """A view to render the contact form page"""
    return render(request, "home/contact.html")