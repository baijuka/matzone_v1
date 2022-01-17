from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, "home/index.html")


def about(request):
    """A view to return the about page"""
    return render(request, "home/about.html")


def contact_submit(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # Send email to customer
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['first_name']
            message = request.POST['message']
            subject = ('We have receiced your message')
            body = render_to_string('home/confirmation_emails/' +
                                    'customer_confirmation_email.txt',
                                    {'first_name': first_name,
                                        'subject': subject,
                                        'message': message,
                                     })

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['baijuka@yahoo.com'],
                fail_silently=False,
            )

            # save message to database
            contact_form.save()

            messages.success(request, 'Your message was sent successfully!')
            return redirect(reverse('contact_submit'))
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')
    else:
        contact_form = ContactForm()

        context = {
            'form': contact_form,
        }

        return render(request, 'home/contact.html', context)